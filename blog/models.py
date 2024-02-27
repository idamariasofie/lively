from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    """
    Model for user profil
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}  Profile'


class Category(models.Model):
    """
    Model for category
    """
    title = models.CharField(max_length=300, unique=True)
    

class Recipe(models.Model):
    """ A model for creating a recipe post """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    content = models.TextField()
    time_to_prepare = models.IntegerField(default=0)
    overview = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)
    featured = models.BooleanField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ Ordering blog posts by created on date """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.recipe.slug])


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
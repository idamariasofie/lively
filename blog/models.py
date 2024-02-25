from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()

# Create your models here.
class Category(models.Model):
    """
    Model for category
    """
    title = models.CharField(max_length=300, unique=True)
    

class Recipe(models.Model):
    """ A model for creating a recipe post """
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipe_author")
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    content = models.TextField()
    time_to_prepare = models.IntegerField(default=0)
    overview = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
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
        return reverse('recipe_detail', kwargs={
            'id': self.id
        })


class Comment(models.Model):
    """ A model to allow and manage comments on recipe blog posts """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                                related_name="comments", null=True)
    name = models.CharField(max_length=80, default='')
    email = models.EmailField(null=True, blank=True, default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Ordering blog comments by created on date """
        ordering = ['-created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.recipe.slug])


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
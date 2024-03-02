from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()

class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    display_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    """
    Model for category
    """
    title = models.CharField(max_length=300, unique=True)
    
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    recipe = models.ForeignKey('blog.Recipe', on_delete=models.CASCADE, null=True, default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        if self.user:
            return f"Comment {self.body} by {self.user.username}"
        else:
            return f"Comment {self.body} by Unknown User"

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.recipe.slug])

class Recipe(models.Model):
    """ A model for creating a recipe post """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name='comments', blank=True)
    comment_count = models.IntegerField(default=0)
    content = models.TextField()
    time_to_prepare = models.IntegerField(default=0)
    overview = models.TextField()
    featured = models.BooleanField()
    status = models.IntegerField(choices=STATUS, default=0)
    photo = models.ImageField(upload_to='recipe_photos/', blank=True, null=True)

    class Meta:
        """ Ordering blog posts by created on date """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

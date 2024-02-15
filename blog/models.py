from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    """ A model for creating a recipe post """
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    content = models.TextField()
    time_to_prepare = models.IntegerField(default=0)
    overview = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    featured = models.BooleanField()
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    """ A model to allow and manage comments on recipe blog posts """
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments", null=True)
    recipe_id = models.CharField(max_length=500)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)



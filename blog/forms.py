from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'comment_count', 'content', 'time_to_prepare', 'overview', 'likes', 'featured')

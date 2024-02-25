from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'created_on')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'created_on', 'comment_count', 'content', 'time_to_prepare', 'overview', 'likes', 'featured')

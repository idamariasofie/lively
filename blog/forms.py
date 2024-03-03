# forms.py
from django import forms
from .models import Comment, Recipe, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'display_name']

class SearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'user')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder'] = 'Add your comment...'

        if user:
            self.fields['user'].initial = Profile.objects.get(user=user)
        else:
            self.fields['user'].queryset = Profile.objects.all()

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'overview', 'content', 'status']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

from .models import Comment, Recipe, Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'display_name']


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=200, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder'] = 'Add your comment...'

        if user:
            # If user is provided, set the initial value and make it a hidden field
            self.fields['user'] = forms.ModelChoiceField(
                queryset=user,
                widget=forms.HiddenInput(),
                initial=user,
            )
        else:
            # If user is not provided, keep it as a regular field
            self.fields['user'] = forms.ModelChoiceField(queryset=user)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'overview', 'content', 'status', 'photo']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
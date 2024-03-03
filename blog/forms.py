class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'user')

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

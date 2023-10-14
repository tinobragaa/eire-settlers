from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    """
    Class that creates a form for the Comment model.
    """
    class Meta:
        model = Comment
        fields = ('body',)

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 4, 'placeholder': 'Add a comment...'}
            ),
        label="",
    )


class ProfileForm(forms.ModelForm):
    """
    Class that creates a form for the Profile model.
    """
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'pronouns',
            'location',
            'nationality',
            'about',
            'image',
            ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "pronouns": "Pronouns",
            "location": "Location",
            "nationality": "Nationality",
            "about": "About",
            "image": "Profile Picture",
        }

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return super().save(commit=commit)

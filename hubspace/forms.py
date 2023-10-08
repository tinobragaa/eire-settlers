from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.ModelForm):
    """
    Form to edit a profile.
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

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return super().save(commit=commit)

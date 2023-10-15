from .models import Comment, Profile, Articles
from django import forms
from crispy_forms.helper import FormHelper

class ArticleForm(forms.ModelForm):
    """
    Form to create and update articles.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = Articles
        fields = [
            'title',
            'excerpt',
            'content',
            'image_preview'
        ]
        labels = {
            "title": "Title",
            "excerpt": "Description",
            "content": "Content",
            'image_preview': "Image",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Article title"}
                ),
            "excerpt": forms.Textarea(
                attrs={"placeholder": "Write a short description"}
                ),
            "content": forms.Textarea(
                attrs={"placeholder": "Enter your article content"}
                ),
        }


class CommentForm(forms.ModelForm):
    """
    Form to create and update comments.
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
    Form to update member profile.
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

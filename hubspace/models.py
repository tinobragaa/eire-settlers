from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

STATUS = ((0, "Draft"), (1, "Published"))


class Articles(models.Model):
    """
    Model class for the articles added to the groups.
    Includes fields for title, member, image, excerpt, content,
    posted date, updated date and status.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="hub_articles"
        )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_preview = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    endorsement = models.ManyToManyField(
        User, related_name="content_endorsement", blank=True)
    saved_items = models.ManyToManyField(
        User, related_name="content_saved", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def endorsement_amount(self):
        return self.endorsement.count()


class Comment(models.Model):
    """
    Model class for comments made on articles.
    """
    article = models.ForeignKey(
        Articles, on_delete=models.CASCADE, related_name="comments")
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="new_comment")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.member.username}"


class Profile(models.Model):
    """
    Model class for user profiles.
    """
    PRONOUN_CHOICES = [
        ('Unspecified', 'None'),
        ('He/Him', 'He/Him'),
        ('She/Her', 'She/Her'),
        ('They/Them', 'They/Them'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    pronouns = models.CharField(
        max_length=15,
        choices=PRONOUN_CHOICES,
        default='Unspecified'
        )
    image = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="static/images/users",
        force_format='WEBP',
        null=True,
        blank=True
        )
    location = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    nationality = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        default='Unspecified'
        )
    about = models.TextField(
        max_length=2000,
        null=True,
        blank=True
        )

    def __str__(self):
        return str(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @property
    def user_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/users/default-profile.webp'

    class Meta:
        ordering = ['-created']

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Articles(models.Model):
    """
    Model class for the artciles added to the groups.
    Includes fields for title, member, image, excerpt, content,
    posted date, updated date, status,
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="articles_added")
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
    Model class for a Comments on Resouces
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
        return f"Comment {self.body} by {self.name}"

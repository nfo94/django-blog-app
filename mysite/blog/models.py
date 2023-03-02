from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    class Meta:
        """This class defines metadata for the model. We use the
        ordering attribute to tell Django that it should sort results by the publish field. This
        ordering will apply by default for database queries when no specific order is provided in
        the query. We indicate descending order by using a hyphen before the field name, -publish.
        Posts will be returned in reverse chronological order by default."""

        ordering = ["-published"]
        indexes = [models.Index(fields=["-published"])]

    def __str__(self):
        return self.title

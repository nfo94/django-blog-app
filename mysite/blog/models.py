from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


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
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """This class defines metadata for the model. We use the
        ordering attribute to tell Django that it should sort results by the publish field. This
        ordering will apply by default for database queries when no specific order is provided in
        the query. We indicate descending order by using a hyphen before the field name, -publish.
        Posts will be returned in reverse chronological order by default."""

        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.title

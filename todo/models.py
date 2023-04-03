from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        default_related_name = "tags"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(to=Tag)

    class Meta:
        default_related_name = "tasks"
        ordering = ["is_done", "deadline"]

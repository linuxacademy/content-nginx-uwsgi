from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from markdownx.utils import markdownify

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField('date created', default=timezone.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def body_html(self):
        return markdownify(self.body)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    updated_date = models.DateField(auto_now_add=True)

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = get_user_model()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .data import ANNOTATIONS
# Create your models here.
class newUsers (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    userid = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

class annotation (models.Model):
    timestamp = models.CharField(max_length=8)
    annotation = models.TextField(blank=False)
    citation = models.CharField(max_length=255)
    author = models.ForeignKey(newUsers, on_delete=models.CASCADE)

class chat (models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, blank=False)
    author = models.ForeignKey(newUsers, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sender = models.CharField(max_length=90)
    receiver = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    subject = models.CharField(max_length=90, blank=True)
    creation_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    read_message = models.BooleanField(default=False)

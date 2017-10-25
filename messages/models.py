from django.db import models
from django.contrib.auth.models import User
from channels.models import Channel


class Message(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)
    created_at = models.DateTimeField(auto_now=True)

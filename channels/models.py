from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChannelUserLink(models.Model):
        user = models.ForeignKey(User)
        channel = models.ForeignKey(Channel)
        STATUS_CHOICES = (
            ('invited', 'invited'),
            ('active', 'active'),
            ('inactive', 'inactive')
        )
        status = models.CharField(choices=STATUS_CHOICES, max_length=8)
        created_at = models.DateTimeField(auto_now=True)
        updated_at = models.DateTimeField(auto_now=True)

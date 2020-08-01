from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Box(models.Model):
    length = models.FloatField(default=0.0)
    breadth = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    area = models.FloatField(default=0.0, null=True, blank=True)
    volume = models.FloatField(default=0.0, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creator.username + '-' + str(self.created_date)

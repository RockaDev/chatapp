from django.db import models
from django.db.models.base import Model
from datetime import datetime
import random

class Room(models.Model):
    name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000000,default="")
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class UserId(models.Model):
    userId = models.CharField(max_length=1000000)
    username = models.CharField(max_length=1000000,default="")
    rooms = models.CharField(max_length=1000000,default="")


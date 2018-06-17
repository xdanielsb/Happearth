from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
User._meta.get_field('email').blank = False

class Item(models.Model):
  code = models.CharField(
      max_length=50, 
      blank=False, 
      unique=True
  )
  desc = models.CharField(
      max_length=256,
      blank=True
  )

class Comment(models.Model):
  desc = models.TextField()
  creation_date = models.DateTimeField(
      auto_now_add=True, 
      blank=True,
      editable=False
  )
  #Foreign keys
  item = models.ForeignKey(
      Item,
      on_delete=models.CASCADE,
      related_name="comments"
  )

class Reaction(models.Model):
  kind = models.CharField(
      max_length=30, 
      blank=False
  )
  desc = models.CharField(
      max_length=256,
      blank=True
  )

class ReactionUser(models.Model):
  item = models.CharField(
      max_length=128,
      blank=False
  )
  creation_date = models.DateTimeField(
      auto_now_add=True,
      blank=True, 
      editable=False
  )
  payload = models.CharField(
      max_length=128, 
      blank=True
  )
  #Foreign keys
  user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE, 
      related_name="reactionUser"
  )
  reaction = models.ForeignKey(
      'accounts.Reaction', 
      on_delete=models.CASCADE,
      related_name="reactions"
  )
  item = models.ForeignKey(
      'accounts.Item',
      on_delete=models.CASCADE,
      related_name="reactions"
  )

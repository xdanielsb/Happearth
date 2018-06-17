from django.db import models
from django.conf import settings
# Create your models here.
class House(models.Model):
  label = models.CharField(max_length=128, blank=False, unique=True)
  creation_date = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
  last_modified = models.DateTimeField(auto_now=True, blank=True)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="house")
  key_app_eco_bee  = models.CharField(max_length=128, blank=True)
  access_token  = models.CharField(max_length=128, blank=True)
  refresh_token  = models.CharField(max_length=128, blank=True)
  expiration_token  = models.CharField(max_length=128, blank=True)
  desc = models.CharField(max_length=256, blank=True)

  def __str__(self):
    pattern = "{} - {}".format(self.label, self.user.username)
    return pattern

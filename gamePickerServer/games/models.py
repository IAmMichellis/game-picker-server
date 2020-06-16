from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
  title = models.TextField()
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

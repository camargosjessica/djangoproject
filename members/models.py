from django.db import models


class Members(models.Model):
  user = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

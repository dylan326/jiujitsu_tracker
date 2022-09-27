from django.db import models

# Create your models here.


class moves(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    position = models.CharField(max_length=64)

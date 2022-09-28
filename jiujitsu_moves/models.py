from django.db import models

# Create your models here.


class moves(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    position = models.CharField(max_length=64)


class bjjmoves(models.Model):
    move_name = models.CharField(max_length=64)
    move_des = models.CharField(max_length=500)
    thoughts = models.CharField(max_length=500)

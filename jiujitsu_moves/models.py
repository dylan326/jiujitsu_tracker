from django.db import models

# Create your models here.


class moves(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    position_id = models.IntegerField()


class bjjmoves(models.Model):
    move_name = models.CharField(max_length=64)
    move_des = models.CharField(max_length=500)
    thoughts = models.CharField(max_length=500)


class classtracker(models.Model):
    date = models.DateField()
    hours = models.CharField(max_length=64)
    number_of_rolls = models.IntegerField()
    

class positions(models.Model):
    position_name = models.CharField(max_length=64)

    
class testtbs1006(models.Model):
    testfield = models.CharField(max_length=64)

from django.db import models

# Create your models here.
class Positions(models.Model):
    position_name = models.CharField(max_length=64)

    def __str__(self):
        return self.position_name

class Moves(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    is_offence = models.BooleanField(default=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, default=1)


class BjjMoves(models.Model):
    move_name = models.CharField(max_length=64)
    move_des = models.CharField(max_length=500)
    thoughts = models.CharField(max_length=500)


class ClassTracker(models.Model):
    date = models.DateField()
    hours = models.CharField(max_length=64)
    number_of_rolls = models.IntegerField()







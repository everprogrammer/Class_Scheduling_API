from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

class Professor(models.Model):
    name = models.CharField(max_length=100)
    courses_taught = models.ManyToManyField(Course)

class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_lab = models.BooleanField(default=False)

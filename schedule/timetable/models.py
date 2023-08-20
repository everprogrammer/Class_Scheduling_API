from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    courses_taught = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} especializes at {self.courses_taught}"

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.start_time}-{self.end_time}'

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time can not be less than end time!')
        return super().clean()

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    is_lab = models.BooleanField(default=False)

    def __str__(self):
        return self.name

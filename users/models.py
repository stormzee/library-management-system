from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

now = timezone.now

class Student(models.Model):

    name = models.CharField(max_length=200)

    Gender = [

        ('Male','Male'),
        ('Female','Female')
    ]

    gender = models.CharField(choices=Gender, max_length=200)
    age = models.DurationField(blank=True, null=True)
    DOB = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.name

    
    def get_age(self):
        self.age = (timezone.now() - self.DOB)/365
        return self.age

    def save(self, *args, **kwargs):
        self.get_age()
        super(Student, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Students'

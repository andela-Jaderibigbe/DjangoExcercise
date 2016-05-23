from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=126, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=126, unique=True)
    classroom = models.ForeignKey(Classroom)

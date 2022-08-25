from tkinter import CASCADE
from django.db import models

# Create your models here.

class Subtopic(models.Model):
    domain = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    subtopic = models.CharField(max_length=200)

class Course(models.Model):
    subtopic_id = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True)
    course_title = models.CharField(max_length=200)
    course_author = models.CharField(max_length=200)
    course_link = models.CharField(max_length=200)
    course_rating = models.IntegerField()
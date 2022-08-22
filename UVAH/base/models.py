from django.db import models

# Create your models here.

class Course(models.Model):
    domain = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    subtopic = models.CharField(max_length=200)
    course_title = models.CharField(max_length=200)
    course_author = models.CharField(max_length=200)
    course_link = models.CharField(max_length=200)
    course_rating = models.IntegerField(max_length=200)
from django.db import models

# Create your models here.
class Domain(models.Model):
    domain_name = models.CharField(max_length=200)
    domain_description = models.TextField(null=True)
    domain_link = models.CharField(max_length=200)

class Topic(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    topic_name = models.CharField(max_length=200)
    topic_description = models.TextField(null=True)
    topic_link = models.CharField(max_length=200)

class Subtopic(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    subtopic_name = models.CharField(max_length=200)
    subtopic_description = models.TextField(null=True)
    subtopic_link = models.CharField(max_length=200)

class Course(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True)
    course_title = models.CharField(max_length=200)
    course_author = models.CharField(max_length=200)
    course_link = models.URLField(max_length=200)
    course_rating = models.IntegerField(null=True, blank=True)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    courses_submitted = models.IntegerField("courses_submitted", null=True, default=0)
    favorite_courses = models.ManyToManyField('Course', related_name="users")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Domain(models.Model):
    domain_name = models.CharField(max_length=200)
    domain_description = models.TextField(null=True)
    domain_link = models.CharField(max_length=200)

    def __str__(self):
        return self.domain_name

class Topic(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    topic_name = models.CharField(max_length=200)
    topic_description = models.TextField(null=True)
    topic_link = models.CharField(max_length=200)

    def __str__(self):
        # return self.topic_name
        return "{} {}".format(self.topic_name, self.domain)

class Subtopic(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    subtopic_name = models.CharField(max_length=200)
    subtopic_description = models.TextField(null=True)
    subtopic_link = models.CharField(max_length=200)

    def __str__(self):
        # return self.subtopic_name
        return "{} {}".format(self.subtopic_name, self.domain)

class Course(models.Model):
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True)
    course_title = models.CharField(max_length=200)
    course_author = models.CharField(max_length=200)
    course_link = models.URLField(max_length=200)
    course_rating = models.IntegerField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.course_title
    # submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
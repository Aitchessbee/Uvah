from ast import Sub
from django.contrib import admin

# Register your models here.

from .models import Course, Subtopic

admin.site.register(Course)
admin.site.register(Subtopic)

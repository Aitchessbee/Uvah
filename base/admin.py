from ast import Sub
from django.contrib import admin

# Register your models here.

from .models import Course, Domain, Topic, Subtopic, CustomUser

admin.site.register(Course)
admin.site.register(Subtopic)
admin.site.register(Domain)
admin.site.register(Topic)
admin.site.register(CustomUser)

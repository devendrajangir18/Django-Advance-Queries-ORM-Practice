# Django-Advance-Queries-ORM-Practice
This app is creted for practice purpose, in this  app i practiced complete django framework strating from basic structure to models, views, templates. further i praticed advance Queries, ORM, database operations, Aggregation and Annotations using django python Shell.

# Custom User model created

# Model Manager Code and Queries for Django shell

is_deleted = models.BooleanField(default=False) 

objects = StudentManager()
admin_objects = models.Manager()

# Queries

from vege.models import *
student = Student.objects.all()

# to change is_delete to False for staring 10 records

for s in Student.objects.all()[10:20]:
...     s.is_deleted = True
...     s.save()
... 

# gives only those recodes from a table which is_deleted = False
students = Student.objects.all()
students.count() 

# To check all recodes in a table including is_deleted = True
Student.admin_objects.all()
Student.admin_objects.all().count()

# Send Email Functionality using Django Smtp server

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "host email address"
EMAIL_HOST_PASSWORD = "password"

# Email Attachmets Functionality added
Using Django EmailMessage class

# Django Signals added 
pre_save, post_save, pre_delete, post_delete


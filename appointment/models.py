from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    date = models.CharField(max_length=100)
    regular_outfit = models.CharField(max_length=100)
    ceremonial_event = models.CharField(max_length=100)
    urban_outfit = models.CharField(max_length=100)
    note = models.TextField()

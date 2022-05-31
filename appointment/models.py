from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time_slot = models.CharField(max_length=100)
    note = models.TimeField()

from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=12)
    department=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Bookings(models.Model):
    booked_by=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=12)
    department=models.CharField(max_length=100)
    event_name=models.CharField(max_length=100)
    event_type=models.CharField(max_length=100)
    event_date=models.DateField()
    event_slot=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

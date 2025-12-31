from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=100)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    hospital = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    needed_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return f"{self.patient_name} needs {self.blood_group}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
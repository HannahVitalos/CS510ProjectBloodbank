from django.core.validators import *
from django.db import models

class BloodTypes(models.TextChoices):
    a_pos = 'A+'
    a_neg = 'A-'
    b_pos = 'B+'
    b_neg = 'B-'
    o_pos = 'O+'
    o_neg = 'O-'
    ab_pos = 'AB+'
    ab_neg = 'AB-'

class OperatingHours(models.Model):
    day = models.CharField(max_length=9, primary_key=True)
    hours = models.CharField(max_length=13)
class BloodBank(models.Model):
    bloodbank_name = models.CharField(max_length=45, primary_key=True)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    day = models.ForeignKey(OperatingHours, on_delete=models.CASCADE)
class Donor(models.Model):
    donor_id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    blood_type = models.CharField(max_length=3, choices=BloodTypes.choices)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    health_interview = models.BooleanField()

class Volunteer(models.Model):
    volunteer_id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    training = models.BooleanField()

class Patient(models.Model):
    patient_id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    blood_type = models.CharField(max_length=3, choices=BloodTypes.choices)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    doctor_name = models.CharField(max_length=45)
    medical_need = models.CharField(max_length=500)

class StaffMember(models.Model):
    staff_id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    hours = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(60)])
    salary = models.IntegerField(validators=[MinValueValidator(15000), MaxValueValidator(500000)])
    bloodbank_name = models.ForeignKey(BloodBank, on_delete=models.CASCADE)

class Donation(models.Model):
    donation_id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BloodTypes.choices)
    date_received = models.DateTimeField()

#class Receives(models.Model): come back

class Login(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
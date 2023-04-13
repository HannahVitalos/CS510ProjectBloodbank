from django.core.validators import *
from django.db import models
from django_cryptography.fields import encrypt

BLOOD_TYPES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

YES_NO_CHOICE = [
    (False, 'No'),
    (True, 'Yes'),
]


class OperatingHours(models.Model):
    day = models.CharField(max_length=9, primary_key=True)
    hours = models.CharField(max_length=13)

    class Meta:
        db_table='OperatingHours'
class BloodBank(models.Model):
    bloodbank_name = models.CharField(max_length=45, primary_key=True)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

    class Meta:
        db_table='Bloodbank'
class Donor(models.Model):
    donor_id = models.AutoField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = encrypt(models.CharField(max_length=45))
    health_interview = models.BooleanField(choices=YES_NO_CHOICE)

    class Meta:
        db_table = 'Donor'


class Volunteer(models.Model):
    volunteer_id = models.AutoField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = encrypt(models.CharField(max_length=45))
    training = models.BooleanField(choices=YES_NO_CHOICE)

    class Meta:
        db_table = 'Volunteer'


class Patient(models.Model):
    patient_id = models.AutoField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    doctor_name = models.CharField(max_length=45)
    medical_need = encrypt(models.CharField(max_length=500))

    class Meta:
        db_table = 'Patient'


class StaffMember(models.Model):
    staff_id = models.AutoField(validators=[MinValueValidator(0)], primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    phone_num = models.CharField(max_length=45)
    address = encrypt(models.CharField(max_length=45))
    position = models.CharField(max_length=45)
    hours = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(60)])
    salary = models.IntegerField(validators=[MinValueValidator(15000), MaxValueValidator(500000)])
    bloodbank_name = models.ForeignKey(BloodBank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'StaffMember'


class Donation(models.Model):
    donation_id = models.AutoField(validators=[MinValueValidator(0)], primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    date_received = models.DateTimeField()

    class Meta:
        db_table = 'Donation'

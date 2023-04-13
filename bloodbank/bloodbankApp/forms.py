from django import forms
from django.forms import ModelForm
from .models import *


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = ('first_name', 'last_name', 'blood_type', 'email', 'phone_num', 'address', 'health_interview')
        labels = {
            'first_name': '',
            'last_name': '',
            'blood_type': 'Select blood type from drop down',
            'email': '',
            'phone_num': '',
            'address': '',
            'health_interview': 'Have you had your health interview?'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address (One line please)'}),
        }


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ('first_name', 'last_name', 'email', 'phone_num', 'address', 'training')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_num': '',
            'address': '',
            'training': 'Have you had any blood donation training?'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address (One line please)'}),
        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'blood_type', 'email', 'phone_num', 'doctor_name', 'medical_need')
        labels = {
            'first_name': '',
            'last_name': '',
            'blood_type': 'Select blood type from drop down',
            'email': '',
            'phone_num': '',
            'doctor_name': '',
            'medical_need': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'medical_need': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the '
                                                                                           'patient\'s medical '
                                                                                           'need.'}),
        }


class StaffMemberForm(ModelForm):
    class Meta:
        model = StaffMember
        fields = ('first_name', 'last_name', 'email', 'phone_num', 'address', 'position', 'hours', 'salary', 'bloodbank_name')
        bloodbank_name: forms.ModelChoiceField(queryset=BloodBank.objects.all().values())
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_num': '',
            'address': '',
            'position': '',
            'hours': '',
            'salary': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address (One line please)'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Position'}),
            'hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weekly Hours'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Salary'}),
        }


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('donor', 'volunteer', 'staff', 'blood_type')
        donor = forms.ModelChoiceField(queryset=Donor.objects.all().values())
        volunteer = forms.ModelChoiceField(queryset=Volunteer.objects.all().values())
        staff = forms.ModelChoiceField(queryset=StaffMember.objects.all().values())
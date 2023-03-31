from django import forms
from django.forms import ModelForm
from .models import *

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

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = ('first_name','last_name','blood_type','email','phone_num','address')
        labels = {
            'first_name': '',
            'last_name': '',
            'blood_type': 'Select blood type from drop down',
            'email': '',
            'phone_num': '',
            'address': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            #'blood_type': forms.Select(choices=BLOOD_TYPES),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address (One line please)'}),
        }
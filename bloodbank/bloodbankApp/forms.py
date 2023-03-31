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

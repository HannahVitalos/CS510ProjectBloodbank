from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *

#views list: homepage (display bloodbank info, login button, donor signup button, volunteer signup button),
#login page, donor sign up page, volunteer sign up page, sign up success page
#signed in views: donors list page, blood list page, patients list page, volunteers list page, recipients list page

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    bloodbank = BloodBank.objects.all().values()
    hours = OperatingHours.objects.all().values()
    return render(request, "bloodbankApp/index.html", {'bloodbank': bloodbank, 'hours': hours})

def donorSign(request):
    submitted = False
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            blood_type = form.cleaned_data['blood_type']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_num']
            address = form.cleaned_data['address']
            interview = form.cleaned_data['health_interview']
            donor = Donor(first_name = fname, last_name = lname, blood_type = blood_type, email = email, phone_num = phone, address = address, health_interview = interview)
            donor.save()
            return HttpResponseRedirect('/donorsignup?submitted=True')
    else:
        form = DonorForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/donorSignUp.html", {'form': form, 'submitted': submitted})

def volunteer(request):
    submitted = False
    if request.method == "POST":
        volForm = VolunteerForm(request.POST)
        if volForm.is_valid():
            fname = volForm.cleaned_data['first_name']
            lname = volForm.cleaned_data['last_name']
            email = volForm.cleaned_data['email']
            phone = volForm.cleaned_data['phone_num']
            address = volForm.cleaned_data['address']
            train = volForm.cleaned_data['training']
            vol = Volunteer(first_name=fname, last_name=lname, email=email, phone_num=phone,
                          address=address, training=train)
            vol.save()
            return HttpResponseRedirect('/volunteersignup?submitted=True')
    else:
        volForm = VolunteerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/volunteer.html", {'volForm': volForm, 'submitted': submitted})

def login(request):
    return render(request, "bloodbankApp/login.html")
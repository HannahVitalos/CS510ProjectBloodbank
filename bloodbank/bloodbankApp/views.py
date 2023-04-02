import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages

# views list: homepage (display bloodbank info, login button, donor signup button, volunteer signup button),
# login page, donor sign up page, volunteer sign up page, sign up success page
# signed in views: donors list page, blood list page, patients list page, volunteers list page, recipients list page

from django.http import HttpResponseRedirect


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
            donor = Donor(first_name=fname, last_name=lname, blood_type=blood_type, email=email, phone_num=phone,
                          address=address, health_interview=interview)
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
        vol_form = VolunteerForm(request.POST)
        if vol_form.is_valid():
            fname = vol_form.cleaned_data['first_name']
            lname = vol_form.cleaned_data['last_name']
            email = vol_form.cleaned_data['email']
            phone = vol_form.cleaned_data['phone_num']
            address = vol_form.cleaned_data['address']
            train = vol_form.cleaned_data['training']
            vol = Volunteer(first_name=fname, last_name=lname, email=email, phone_num=phone,
                            address=address, training=train)
            vol.save()
            return HttpResponseRedirect('/volunteersignup?submitted=True')
    else:
        vol_form = VolunteerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/volunteer.html", {'volForm': vol_form, 'submitted': submitted})


def donation(request):
    submitted = False
    if request.method == "POST":
        donation_form = DonationForm(request.POST)
        if donation_form.is_valid():
            donor = donation_form.cleaned_data['donor']
            vol = donation_form.cleaned_data['volunteer']
            staff = donation_form.cleaned_data['staff']
            blood = donation_form.cleaned_data['blood_type']
            current = datetime.datetime.now()
            new_donation = Donation(donor=donor, volunteer=vol, staff=staff, blood_type=blood, date_received=current)
            new_donation.save()
            return HttpResponseRedirect('/adddonation?submitted=True')
    else:
        donation_form = DonationForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "bloodbankApp/donation.html", {'form': donation_form, 'submitted': submitted})


def patient(request):
    submitted = False
    if request.method == "POST":
        p_form = PatientForm(request.POST)
        if p_form.is_valid():
            fname = p_form.cleaned_data['first_name']
            lname = p_form.cleaned_data['last_name']
            blood = p_form.cleaned_data['blood_type']
            email = p_form.cleaned_data['email']
            phone = p_form.cleaned_data['phone_num']
            doctor = p_form.cleaned_data['doctor_name']
            notes = p_form.cleaned_data['medical_notes']
            new_patient = Patient(first_name=fname, last_name=lname, blood_type=blood, email=email, phone_num=phone,
                                  doctor_name=doctor, medical_notes=notes)
            new_patient.save()
            return HttpResponseRedirect('/volunteersignup?submitted=True')
    else:
        p_form = PatientForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/patient.html", {'form': p_form, 'submitted': submitted})


def update(request, table_name, pri_k):
    table = table_name
    object = None
    form = None
    if table == 'donor':
        object = Donor.objects.get(pk=pri_k)
        form = DonorForm(request.POST or None, instance=object)
    elif table == 'volunteer':
        object = Volunteer.objects.get(pk=pri_k)
        form = VolunteerForm(request.POST or None, instance=object)
    elif table == 'patient':
        object = Patient.objects.get(pk=pri_k)
        form = PatientForm(request.POST or None, instance=object)
    elif table == 'staffmember':
        object = StaffMember.objects.get(pk=pri_k)
        form = StaffMemberForm(request.POST or None, instance=object)
    elif table == 'donation':
        object = Donation.objects.get(pk=pri_k)
        form = DonationForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('table', table_name=table_name)
    return render(request, "update.html", {'table_name': table_name, 'pri_k': pri_k, 'object': object, 'form': form})

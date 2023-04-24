import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages

# views list: homepage (display bloodbank info, login button, donor signup button, volunteer signup button),
# login page, donor sign up page, volunteer sign up page, sign up success page
# signed in views: donors list page, blood list page, patients list page, volunteers list page, recipients list page

from django.http import HttpResponseRedirect


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "bloodbankApp/index.html", {"fname": fname})
        else:
            # messages.error(request, "Login failed: invalid username or password")
            redirect('home')
    return render(request, "login.html")


def signout(request):
    logout(request)
    # message success here
    return redirect('home')


def index(request):
    bloodbank = BloodBank.objects.all().values()
    hours = OperatingHours.objects.all().values()
    return render(request, "bloodbankApp/index.html", {'bloodbank': bloodbank, 'hours': hours})


@login_required
def show_table(request, table_name):
    table = table_name
    objects = None
    if table == 'donor':
        objects = Donor.objects.all()
    elif table == 'volunteer':
        objects = Volunteer.objects.all()
    elif table == 'patient':
        objects = Patient.objects.all()
    elif table == 'staffmember':
        objects = StaffMember.objects.all()
    elif table == 'donation':
        objects = Donation.objects.all()
    objects_list = list(objects.values())
    return render(request, "bloodbankApp/table.html", {'table_name': table_name, 'objects': objects_list})


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


@login_required
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


@login_required
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
            notes = p_form.cleaned_data['medical_need']
            new_patient = Patient(first_name=fname, last_name=lname, blood_type=blood, email=email, phone_num=phone,
                                  doctor_name=doctor, medical_need=notes)
            new_patient.save()
            return HttpResponseRedirect('/addpatient?submitted=True')
    else:
        p_form = PatientForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/patient.html", {'form': p_form, 'submitted': submitted})


@login_required
def staff(request):
    submitted = False
    if request.method == "POST":
        s_form = StaffMemberForm(request.POST)
        if s_form.is_valid():
            fname = s_form.cleaned_data['first_name']
            lname = s_form.cleaned_data['last_name']
            email = s_form.cleaned_data['email']
            phone = s_form.cleaned_data['phone_num']
            address = s_form.cleaned_data['address']
            position = s_form.cleaned_data['position']
            hours = s_form.cleaned_data['hours']
            salary = s_form.cleaned_data['salary']
            bank_name = s_form.cleaned_data['bloodbank_name']
            staff = StaffMember(first_name=fname, last_name=lname, email=email, phone_num=phone,
                                address=address, position=position, hours=hours, salary=salary,
                                bloodbank_name=bank_name)
            staff.save()
            return HttpResponseRedirect('/addstaffmember?submitted=True')
    else:
        s_form = StaffMemberForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "bloodbankApp/staffmember.html", {'sForm': s_form, 'submitted': submitted})


@login_required
def update(request, table_name, pri_k):
    table = table_name
    item = None
    form = None
    if table == 'donor':
        item = Donor.objects.get(pk=pri_k)
        form = DonorForm(request.POST or None, instance=item)
    elif table == 'volunteer':
        item = Volunteer.objects.get(pk=pri_k)
        form = VolunteerForm(request.POST or None, instance=item)
    elif table == 'patient':
        item = Patient.objects.get(pk=pri_k)
        form = PatientForm(request.POST or None, instance=item)
    elif table == 'staffmember':
        item = StaffMember.objects.get(pk=pri_k)
        form = StaffMemberForm(request.POST or None, instance=item)
    elif table == 'donation':
        item = Donation.objects.get(pk=pri_k)
        form = DonationForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('table', table_name=table_name)
    return render(request, "update.html", {'table_name': table_name, 'pri_k': pri_k, 'object': item, 'form': form})


@login_required
def remove(request, table_name, pri_k):
    table_name = table_name
    table = None
    item = None
    if table_name == 'donor':
        table = Donor
    elif table_name == 'volunteer':
        table = Volunteer
    elif table_name == 'patient':
        table = Patient
    elif table_name == 'staffmember':
        table = StaffMember
    elif table_name == 'donation':
        table = Donation
    if table.objects.filter(pk=pri_k):
        item = table.objects.get(pk=pri_k)
        item.delete()
        messages.success(request, "Item successfully removed")
        return redirect('table', table_name=table_name)
    else:
        messages.error(request, "Item could not be removed")
        return redirect('table', table_name=table_name)
    return render(request, "table.html", {'table_name': table_name, 'pri_k': pri_k, 'object': item})


@login_required
def search(request, table_name):
    table_name = table_name
    items = None
    if request.method == "GET":
        to_find = request.GET['to_find']
        if table_name == 'donor':
            items = Donor.objects.filter(
                Q(donor_id__icontains=to_find) | Q(first_name__icontains=to_find) | Q(
                    last_name__icontains=to_find) | Q(blood_type__icontains=to_find) | Q(
                    email__icontains=to_find) | Q(phone_num__icontains=to_find) | Q(
                    health_interview__icontains=to_find))
        elif table_name == 'volunteer':
            items = Volunteer.objects.all().values()
            items = Volunteer.objects.filter(
                Q(volunteer_id__icontains=to_find) | Q(first_name__icontains=to_find) | Q(
                    last_name__icontains=to_find) | Q(
                    email__icontains=to_find) | Q(phone_num__icontains=to_find) | Q(
                    training__icontains=to_find))
        elif table_name == 'patient':
            items = Patient.objects.all().values()
            items = Patient.objects.filter(
                Q(patient_id__icontains=to_find) | Q(first_name__icontains=to_find) | Q(
                    last_name__icontains=to_find) | Q(blood_type__icontains=to_find) | Q(
                    email__icontains=to_find) | Q(phone_num__icontains=to_find) | Q(doctor_name__icontains=to_find))
        elif table_name == 'staffmember':
            items = StaffMember.objects.all().values()
            items = StaffMember.objects.filter(
                Q(staff_id__icontains=to_find) | Q(first_name__icontains=to_find) | Q(
                    last_name__icontains=to_find) | Q(
                    email__icontains=to_find) | Q(phone_num__icontains=to_find) | Q(
                    position__icontains=to_find) | Q(hours__icontains=to_find) | Q(salary__icontains=to_find) | Q(
                    bloodbank_name__icontains=to_find))
        elif table_name == 'donation':
            items = Donation.objects.all().values()
            items = Donation.objects.filter(
                Q(donation_id__icontains=to_find) | Q(donor__icontains=to_find) | Q(
                    volunteer__icontains=to_find) | Q(blood_type__icontains=to_find) | Q(
                    staff__icontains=to_find) | Q(date_received__icontains=to_find))
        items_list = list(items.values())
        return render(request, "search.html", {"table_name": table_name, "to_find": to_find, 'objects': items_list})
    else:
        return render(request, "search.html", {"table_name": table_name})

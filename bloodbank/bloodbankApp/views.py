from django.shortcuts import render

#views list: homepage (display bloodbank info, login button, donor signup button, volunteer signup button),
#login page, donor sign up page, volunteer sign up page, sign up success page
#signed in views: donors list page, blood list page, patients list page, volunteers list page, recipients list page

from django.http import HttpResponse


def index(request):
    return render(request, "bloodbankApp/index.html")
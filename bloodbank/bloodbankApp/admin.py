from django.contrib import admin

from .models import *

admin.site.register(OperatingHours)
admin.site.register(BloodBank)
admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(Patient)
admin.site.register(StaffMember)
admin.site.register(Donation)
admin.site.register(Login)
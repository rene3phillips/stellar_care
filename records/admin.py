from django.contrib import admin
from .models import Doctor, Patient, Appointment, Billing

class DoctorAdmin(admin.ModelAdmin):
    ordering = ['last_name', 'first_name']

class PatientAdmin(admin.ModelAdmin):
    ordering = ['last_name', 'first_name']

class AppointmentAdmin(admin.ModelAdmin):
    ordering = ['appointment_date']

class BillingAdmin(admin.ModelAdmin):
    ordering = ['appointment__patient__last_name']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Billing, BillingAdmin)
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_hired = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    patients = models.ManyToManyField('Patient', related_name='doctors', through='Appointment')

    # Drop-down menus
    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialty})"
    
class Patient(models.Model):

    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unknown"),
        ("O", "Other"),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    sex  = models.CharField(max_length=2, choices=SEX_CHOICES, default="U")
    emergency_contact = models.CharField(max_length = 100, null=True, blank=True)
    insurance_number = models.CharField(max_length=50, null=True, blank=True)
    allergies = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Appointment(models.Model):

    DURATION_CHOICES = [
        (15, '15 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '60 minutes'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    duration = models.PositiveIntegerField(choices=DURATION_CHOICES, default=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.appointment_date.strftime('%B %d, %Y')} - {self.patient.first_name} {self.patient.last_name} with Dr. {self.doctor.first_name} {self.doctor.last_name}"

class Billing(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_billed = models.DateField(default=timezone.now)
    due_date = models.DateField(default=timezone.now() + timedelta(days=30))
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Overdue', 'Overdue')], default='Pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        patient = self.appointment.patient
        return f"{patient.last_name}, {patient.first_name}: {self.total_amount} ({self.payment_status})"
    
    class Meta:
        verbose_name_plural = "Billing"
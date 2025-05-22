from django.db import models
from django.conf import settings

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    patients = models.ManyToManyField('Patient', related_name='doctors', through='Appointment')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialty})"

class Patient(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    sex  = models.CharField(max_length=2, choices=[("M", "Male"), ("F", "Female"), ("U", "Unknown"), ("O", "Other"), ], null=True, blank=True)
    emergency_contact = models.CharField(max_length = 100, null=True, blank=True)
    insurance_number = models.CharField(max_length=50, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    diagnosis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.appointment_date.strftime('%B %d, %Y')} - {self.patient.first_name} {self.patient.last_name} with Dr. {self.doctor.first_name} {self.doctor.last_name}"

class Billing(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Overdue', 'Overdue')], default='Pending')

    def __str__(self):
        patient = self.appointment.patient
        return f"{patient.last_name}, {patient.first_name}: {self.total_amount} ({self.payment_status})"
    
    class Meta:
        verbose_name_plural = "Billing"
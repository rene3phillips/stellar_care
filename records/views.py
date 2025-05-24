from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient, Doctor, Appointment, Billing
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BillingForm

# Patient views

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'records/patient/patient_list.html'
    context_object_name = 'patients' 

    def get_queryset(self):
        return Patient.objects.order_by('last_name', 'first_name')

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'records/patient/patient_detail.html'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'sex', 'emergency_contact', 'insurance_number', 'allergies', 'medical_history'] 
    template_name = 'records/patient/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

    # Override form_valid method to set the owner of this model object to the current logged-in user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'sex', 'emergency_contact', 'insurance_number', 'allergies', 'medical_history'] 
    template_name = 'records/patient/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

    # Override test_func method to determine if current user is staff (can login to Django admin dashboard) or the owner
    def test_func(self):
        patient = self.get_object()
        return self.request.user.is_staff or patient.owner == self.request.user

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = 'records/patient/patient_confirm_delete.html'
    success_url = reverse_lazy('records:patient_list')

    def test_func(self):
        patient = self.get_object()
        return self.request.user.is_staff or patient.owner == self.request.user
    
# Doctor views

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'records/doctor/doctor_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        return Doctor.objects.order_by('last_name', 'first_name')

class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'records/doctor/doctor_detail.html'

class DoctorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'email', 'phone_number', 'date_hired', 'license_number', 'is_active', 'notes']
    template_name = 'records/doctor/doctor_form.html'
    success_url = reverse_lazy('records:doctor_list')

    def test_func(self):
        return self.request.user.is_staff

class DoctorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'email', 'phone_number', 'date_hired', 'license_number', 'is_active', 'notes']
    template_name = 'records/doctor/doctor_form.html'
    success_url = reverse_lazy('records:doctor_list')

    def test_func(self):
        return self.request.user.is_staff

class DoctorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Doctor
    template_name = 'records/doctor/doctor_confirm_delete.html'
    success_url = reverse_lazy('records:doctor_list')

    def test_func(self):
        return self.request.user.is_staff
    
# Appointment views

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'records/appointment/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.order_by('patient__last_name', 'patient__first_name', 'appointment_date')

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'records/appointment/appointment_detail.html'

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'duration', 'status', 'notes']
    template_name = 'records/appointment/appointment_form.html'
    success_url = reverse_lazy('records:appointment_list')

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'duration', 'status', 'notes']
    template_name = 'records/appointment/appointment_form.html'
    success_url = reverse_lazy('records:appointment_list')

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'records/appointment/appointment_confirm_delete.html'
    success_url = reverse_lazy('records:appointment_list')

# Billing views

class BillingListView(LoginRequiredMixin, ListView):
    model = Billing
    template_name = 'records/billing/billing_list.html'
    context_object_name = 'billings'

    def get_queryset(self):
        return Billing.objects.order_by('appointment__patient__last_name', 'appointment__patient__first_name', 'appointment__appointment_date')

class BillingDetailView(LoginRequiredMixin, DetailView):
    model = Billing
    template_name = 'records/billing/billing_detail.html'

class BillingCreateView(LoginRequiredMixin, CreateView):
    model = Billing
    form_class = BillingForm
    # fields = ['appointment', 'total_amount', 'payment_status']
    template_name = 'records/billing/billing_form.html'
    success_url = reverse_lazy('records:billing_list')

class BillingUpdateView(LoginRequiredMixin, UpdateView):
    model = Billing
    fields = ['appointment', 'total_amount', 'payment_status', 'date_billed', 'due_date', 'notes']
    template_name = 'records/billing/billing_form.html'
    success_url = reverse_lazy('records:billing_list')

class BillingDeleteView(LoginRequiredMixin, DeleteView):
    model = Billing
    template_name = 'records/billing/billing_confirm_delete.html'
    success_url = reverse_lazy('records:billing_list')
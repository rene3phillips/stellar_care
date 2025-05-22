from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'records/patient_list.html'
    context_object_name = 'patients' 

    def get_queryset(self):
        return Patient.objects.order_by('last_name')

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'records/patient_detail.html'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] 
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

    # Override form_valid method to set the owner of this model object to the current logged-in user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] 
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

    # Override test_func method to determine if current user is staff (can login to Django admin dashboard) or the owner
    def test_func(self):
        patient = self.get_object()
        return self.request.user.is_staff or patient.owner == self.request.user

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = 'records/patient_confirm_delete.html'
    success_url = reverse_lazy('records:patient_list')

    def test_func(self):
        patient = self.get_object()
        return self.request.user.is_staff or patient.owner == self.request.user
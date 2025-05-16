from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'records/patient_list.html'
    context_object_name = 'patients' # 'for patient in patients' vs 'for patient in object_list'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'records/patient_detail.html'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] # which fields to include
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') # where to redirect 

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] 
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

    def test_func(self):
        return self.request.user.is_staff

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = 'records/patient_confirm_delete.html'
    success_url = reverse_lazy('records:patient_list')

    def test_func(self):
        return self.request.user.is_staff
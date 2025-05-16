from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'records/patient_list.html'
    context_object_name = 'patients' # 'for patient in patients' vs 'for patient in object_list'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'records/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] # which fields to include
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') # where to redirect 

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth'] 
    template_name = 'records/patient_form.html'
    success_url = reverse_lazy('records:patient_list') 

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'records/patient_confirm_delete.html'
    success_url = reverse_lazy('records:patient_list')
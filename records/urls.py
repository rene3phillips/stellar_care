from django.urls import path
from django.views.generic import RedirectView
from .views import (
    PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,
    BillingListView, BillingDetailView, BillingCreateView, BillingUpdateView, BillingDeleteView
)

app_name = 'records'

urlpatterns = [
    path('', RedirectView.as_view(url='patients/', permanent=False)),
    path('patients/', PatientListView.as_view(), name='patient_list'), # name allows you to refer to this URL in templates and redirects
    path('patients/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),

    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('billing/', BillingListView.as_view(), name='billing_list'),
    path('billing/create/', BillingCreateView.as_view(), name='billing_create'),
    path('billing/<int:pk>/', BillingDetailView.as_view(), name='billing_detail'),
    path('billing/<int:pk>/update/', BillingUpdateView.as_view(), name='billing_update'),
    path('billing/<int:pk>/delete/', BillingDeleteView.as_view(), name='billing_delete'),
]
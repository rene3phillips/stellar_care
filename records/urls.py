from django.urls import path
from .views import (
    PatientListView,
    PatientDetailView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
)

app_name = 'records'

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'), # name allows you to refer to this URL in templates and redirects
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<int:pk>/update', PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete', PatientDeleteView.as_view(), name='patient_delete'),
]
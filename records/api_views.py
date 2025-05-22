from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer
from .permissions import IsOwnerOrReadOnly

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-id')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['owner', 'first_name', 'last_name', 'date_of_birth']
    search_fields = ['first_name', 'last_name', 'date_of_birth']
    ordering_fields = ['first_name', 'last_name', 'date_of_birth']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
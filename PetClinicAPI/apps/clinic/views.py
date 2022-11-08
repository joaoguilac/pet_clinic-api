from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from PetClinicAPI.apps.clinic.models import Drug, Appointment
from PetClinicAPI.apps.clinic.serializers import DrugSerializer, AppointmentSerializer
from PetClinicAPI.resources.permissions import IsVetOrAdminOrReadOnly, IsVeterinartOrIsAuthenticatedReadOnly

class DrugViewSet(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsVetOrAdminOrReadOnly]

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsVeterinartOrIsAuthenticatedReadOnly]
from rest_framework.viewsets import ModelViewSet

from PetClinicAPI.apps.clinic.models import Veterinary, Drug, Appointment
from PetClinicAPI.apps.clinic.serializers import VeterinarySerializer, DrugSerializer, AppointmentSerializer

class VeterinaryViewSet(ModelViewSet):
    queryset = Veterinary.objects.all()
    serializer_class = VeterinarySerializer

class DrugViewSet(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
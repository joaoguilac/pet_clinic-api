from rest_framework.viewsets import ModelViewSet

from PetClinicAPI.apps.clinic.models import Veterinary, Drug, Appointment

class VeterinaryViewSet(ModelViewSet):
    queryset = Veterinary.objects.all()

class DrugViewSet(ModelViewSet):
    queryset = Drug.objects.all()

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()

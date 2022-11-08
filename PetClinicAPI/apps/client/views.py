from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from PetClinicAPI.apps.client.models import Client, Pet, Address
from PetClinicAPI.apps.client.serializers import ClientSerializer, PetSerializer, AddressSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import serializers

from PetClinicAPI.apps.clinic.models import Veterinary, Drug, Appointment
from PetClinicAPI.apps.client.serializers import PetSerializer

class VeterinarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=255)

    class Meta:
        model = Veterinary
        fields = ('id', 'name', 'email', 'phone')
        ref_name = None

class DrugSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Drug
        fields = ('id', 'name')
        ref_name = None

class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    date = serializers.DateField()
    description = serializers.CharField(max_length=255)
    diagnosis = serializers.CharField(max_length=255)
    drugs = DrugSerializer(many=True, read_only=True)
    drugs_id = serializers.UUIDField(many=True, write_only=True)
    pet = PetSerializer(read_only=True)
    pet_id = serializers.UUIDField(write_only=True)
    veterinary = VeterinarySerializer(read_only=True)
    veterinary_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        ref_name = None
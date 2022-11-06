from rest_framework import serializers

from PetClinicAPI.apps.client.models import Veterinary, Drug, Appointment

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
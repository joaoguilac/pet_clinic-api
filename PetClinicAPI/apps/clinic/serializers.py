from rest_framework import serializers

from PetClinicAPI.apps.clinic.models import Drug, Appointment, Avaliation
from PetClinicAPI.apps.client.serializers import PetSerializer
from PetClinicAPI.apps.authentication.serializers import UserSerializer


class DrugSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Drug
        fields = ('id', 'name')
        ref_name = None

class AvaliationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    rating = serializers.IntegerField(max_value=5, min_value=0)

    class Meta:
        model = Avaliation
        fields = '__all__'
        ref_name = None

class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    date = serializers.DateField()
    description = serializers.CharField(max_length=255)
    diagnosis = serializers.CharField(max_length=255)
    drugs = DrugSerializer(many=True, read_only=True)
    drugs_ids = serializers.ListField(child=serializers.UUIDField(), write_only=True)
    pet = PetSerializer(read_only=True)
    pet_id = serializers.UUIDField(write_only=True)
    veterinary = UserSerializer(read_only=True)
    avaliation = AvaliationSerializer(read_only=True)

    def create(self, validated_data):
        veterinary_id = self.context['request'].user.id
        validated_data['veterinary_id'] = veterinary_id
        drugs_id = validated_data.pop('drugs_ids')
        appointment = super(AppointmentSerializer, self).create(validated_data)
        appointment.drugs.set(drugs_id)
        appointment.save()

        return appointment

    def update(self, instance, validated_data):
        veterinary_id = self.context['request'].user.id
        validated_data['veterinary_id'] = veterinary_id
        appointment = super(AppointmentSerializer, self).update(instance, validated_data)
        appointment.drugs.set(validated_data['drugs_ids'])
        appointment.save()

        return appointment

    class Meta:
        model = Appointment
        fields = '__all__'
        ref_name = None

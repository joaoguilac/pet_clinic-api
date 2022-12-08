from rest_framework import serializers

from PetClinicAPI.apps.client.models import Address, Client, Pet


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    district = serializers.CharField(max_length=255)
    zip = serializers.CharField(max_length=9)

    class Meta:
        model = Address
        fields = "__all__"
        ref_name = None


class PetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    breed = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    owner_id = serializers.UUIDField()
    owner_name = serializers.CharField(
        max_length=255, read_only=True, source="owner.name"
    )

    class Meta:
        model = Pet
        fields = ("id", "name", "breed", "birth_date", "owner_id", "owner_name")
        ref_name = None


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    address = AddressSerializer(read_only=True)
    address_id = serializers.UUIDField(write_only=True)
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
        ref_name = None

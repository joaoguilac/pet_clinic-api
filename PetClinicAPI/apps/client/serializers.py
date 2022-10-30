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
        fields = ('id', 'street', 'city', 'state', 'district', 'zip')
        ref_name = None

class PetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    breed = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    owner_id = serializers.UUIDField()

    class Meta:
        model = Pet
        fields = ('id', 'name', 'breed', 'birth_date', 'owner_id')
        ref_name = None

class ClientSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    address = AddressSerializer()
    pets = PetSerializer(many=True, read_only=True)

    def create(self, validated_data):
        address = validated_data.pop('address')
        address = Address.objects.create(**address)
        client = Client.objects.create(address=address, **validated_data)
        return client

    def update(self, instance, validated_data):
        address = validated_data.pop('address')
        address = Address.objects.update(**address)
        client = Client.objects.update(address=address, **validated_data)
        return client

    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'email', 'address', 'pets')
        ref_name = None


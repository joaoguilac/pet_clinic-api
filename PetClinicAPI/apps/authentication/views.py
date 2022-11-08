from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from PetClinicAPI.resources.permissions import IsAdminForRegisterAndIsOwnerToEdit

from PetClinicAPI.apps.authentication.models import User
from PetClinicAPI.apps.authentication.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminForRegisterAndIsOwnerToEdit]
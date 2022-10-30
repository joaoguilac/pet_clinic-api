from rest_framework.viewsets import ModelViewSet

from PetClinicAPI.resources.permissions import IsOwnerOrReadOnly

from PetClinicAPI.apps.authentication.models import User
from PetClinicAPI.apps.authentication.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
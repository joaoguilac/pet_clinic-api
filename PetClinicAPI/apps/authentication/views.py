from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from PetClinicAPI.resources.permissions import IsAdminForRegisterAndIsOwnerToEdit

from PetClinicAPI.apps.authentication.models import User
from PetClinicAPI.apps.authentication.serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminForRegisterAndIsOwnerToEdit]

    def get_queryset(self):
        params = self.request.query_params
        role_filter = params.get("role")
        if role_filter:
            return super().get_queryset().filter(role=role_filter)
        return super().get_queryset()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

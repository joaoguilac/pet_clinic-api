from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.client.views import ClientViewSet, PetViewSet, AddressViewSet

router = SimpleRouter()
router.register('pets', PetViewSet, basename='pets')
router.register('address', AddressViewSet, basename='address')
router.register('', ClientViewSet, basename='clients')

urlpatterns = router.urls
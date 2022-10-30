from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.client.views import ClientViewSet, PetViewSet

router = SimpleRouter()
router.register('pets', PetViewSet, basename='pets')
router.register('', ClientViewSet, basename='clients')

urlpatterns = router.urls
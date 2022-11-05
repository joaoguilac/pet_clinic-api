from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.client.views import ClientViewSet, PetViewSet

router = SimpleRouter()
router.register('', ClientViewSet, basename='clients')
router.register('pets', PetViewSet, basename='pets')

urlpatterns = router.urls
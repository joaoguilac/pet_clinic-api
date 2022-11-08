from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.clinic.views import DrugViewSet, AppointmentViewSet, AvaliationViewSet

router = SimpleRouter()
router.register('drugs', DrugViewSet, basename='drugs')
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('avaliations', AvaliationViewSet, basename='avaliation')

urlpatterns = router.urls
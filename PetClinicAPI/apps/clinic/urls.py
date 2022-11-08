from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.clinic.views import DrugViewSet, AppointmentViewSet

router = SimpleRouter()
router.register('drugs', DrugViewSet, basename='drugs')
router.register('appointments', AppointmentViewSet, basename='appointments')

urlpatterns = router.urls
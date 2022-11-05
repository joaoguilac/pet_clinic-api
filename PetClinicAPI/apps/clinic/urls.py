from rest_framework.routers import SimpleRouter

from PetClinicAPI.apps.clinic.views import VeterinaryViewSet, DrugViewSet, AppointmentViewSet

router = SimpleRouter()
router.register('veterinaries', VeterinaryViewSet, basename='veterinaries')
router.register('drugs', DrugViewSet, basename='drugs')
router.register('appointments', AppointmentViewSet, basename='appointments')

urlpatterns = router.urls
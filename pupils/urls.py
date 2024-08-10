from .views import PupilViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pupils', PupilViewSet, basename='pupils')

urlpatterns = router.urls
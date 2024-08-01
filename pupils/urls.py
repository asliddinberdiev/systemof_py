from rest_framework.routers import SimpleRouter
from .views import PupilViewSet

router = SimpleRouter()
router.register('pupils', PupilViewSet, basename='pupils')


urlpatterns = router.urls

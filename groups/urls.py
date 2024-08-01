from rest_framework.routers import SimpleRouter
from .views import GroupViewSet

router = SimpleRouter()
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = router.urls
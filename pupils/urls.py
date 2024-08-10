from django.urls import path
from .views import PupilViewSet  # Ensure PupilViewSet is imported from the correct module
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pupils', PupilViewSet, basename='pupils')

urlpatterns = router.urls + [
    # Manually add the export_excel route
    path('pupils/export_excel/', PupilViewSet.as_view({'get': 'export_excel'}), name='pupil-export-excel'),
]

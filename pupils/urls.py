from django.urls import path
from .views import PupilList, PupilDetail

urlpatterns = [
    path("", PupilList.as_view()),
    path("<int:pk>/", PupilDetail.as_view())
]

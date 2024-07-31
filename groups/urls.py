from django.urls import path
from .views import GroupList, GroupDetail

urlpatterns = [
    path("", GroupList.as_view()),
    path("<int:pk>/", GroupDetail.as_view())
]

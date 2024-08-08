from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import GroupSerializer
from .models import Group

# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (SearchFilter,)
    search_fields = ["name", "start_time", "end_time",]



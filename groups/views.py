from rest_framework.viewsets import ModelViewSet
from .serializers import GroupSerializer
from .models import Group

# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



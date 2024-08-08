from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import PupilSerializer
from .models import Pupil

# Create your views here.
class PupilViewSet(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    filter_backends = (SearchFilter,)
    search_fields = ["firstname", "lastname", "pupil_phone", "parent_phone" ]




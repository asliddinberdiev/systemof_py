from .serializers import PupilSerializer
from rest_framework.viewsets import ModelViewSet 
from .models import Pupil

# Create your views here.
class PupilViewSet(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer




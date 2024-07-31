from .serializers import PupilSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pupil

# Create your views here.
class PupilList(ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

class PupilDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer


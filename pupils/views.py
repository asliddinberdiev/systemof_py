import pandas as pd
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Pupil
from .serializers import PupilSerializer

class PupilViewSet(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    filter_backends = (SearchFilter,)
    search_fields = ["firstname", "lastname", "pupil_phone", "parent_phone", "group__name"]

    def export_excel(self, request, *args, **kwargs):
        # Retrieve filtered Pupil records
        pupils = self.filter_queryset(self.get_queryset())

        # Serialize the queryset
        pupil_data = PupilSerializer(pupils, many=True).data

        # Convert to DataFrame
        df = pd.DataFrame(pupil_data)

        # Create an HttpResponse object with Excel MIME type
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=pupils.xlsx'

        # Write the DataFrame to the response
        df.to_excel(response, index=False, engine='openpyxl')

        return response

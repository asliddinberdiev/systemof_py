from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from .models import Pupil
from .serializers import PupilSerializer
import os
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from django.utils.crypto import get_random_string
import threading

class PupilViewSet(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    filter_backends = (SearchFilter,)
    search_fields = ["firstname", "lastname", "pupil_phone", "parent_phone", "group__name"]

    @action(detail=False, methods=['get'])
    def export_excel(self, request):
        pupils = self.get_queryset()
        pupil_list = []

        for index, pupil in enumerate(pupils):
            pupil_list.append({
                "id": index + 1,
                "firstname": pupil.firstname,
                "lastname": pupil.lastname,
                "group": pupil.group.name if pupil.group else '',  # Assuming 'group' is a ForeignKey
                "pupil_phone": pupil.pupil_phone,
                "parent_phone": pupil.parent_phone,
            })

        # Create a random filename
        filename = f'pupils_{get_random_string(8)}.xls'
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Create an Excel writer using xlsxwriter engine
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            df = pd.DataFrame(pupil_list)
            df.to_excel(writer, index=False)

            # Get the workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            # Define a format for centering text
            center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

            # Set the column width and apply the center alignment to all cells
            for i, col in enumerate(df.columns):
                max_len = df[col].astype(str).map(len).max() + 5  # Adjust the padding value as needed
                worksheet.set_column(i, i, max_len, center_format)

            # Center align the header row as well
            worksheet.set_row(0, None, center_format)

        # Create a URL to download the file
        file_url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        # Schedule deletion of the file after 1 minute
        threading.Timer(60.0, delete_file, [file_path]).start()

        return JsonResponse({
            'status': 200,
            'file_url': file_url
        })

def delete_file(file_path):
    """Delete the file from the file system."""
    if os.path.exists(file_path):
        os.remove(file_path)
import pandas as pd
import sqlite3
from io import BytesIO
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
        # Connect to the SQLite database
        connection = sqlite3.connect("../db.sqlite3")

        # Construct your SQL query to get the Pupil data
        query = """
            SELECT 
                mainTable.*, 
                secondaryTable.someColumn 
            FROM 
                mainTable 
            LEFT JOIN 
                secondaryTable 
            ON 
                mainTable.Id = secondaryTable.mainId
        """

        # Fetch the data into a DataFrame
        df = pd.read_sql(query, connection)

        # Save DataFrame to a BytesIO object
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        # Create an HttpResponse object with Excel MIME type
        response = HttpResponse(output,
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=pupils.xlsx'

        # Close the database connection
        connection.close()

        return response

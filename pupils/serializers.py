from rest_framework import serializers
from .models import Pupil


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Pupil

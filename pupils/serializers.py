from rest_framework import serializers
from .models import Pupil


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ('__all__')

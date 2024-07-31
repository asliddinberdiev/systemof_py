from rest_framework import serializers
from .models import Pupil


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'group', 'pupil_phone', 'parent_phone', 'image', 'created_at', 'updated_at')
        model = Pupil

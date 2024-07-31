from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'start_time', 'end_time', 'created_at', 'updated_at')
        model = Group

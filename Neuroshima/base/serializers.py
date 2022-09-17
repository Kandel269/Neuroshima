from rest_framework import serializers
from .models import Armies


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    data_create = serializers.DateTimeField()
    data_updated = serializers.DateTimeField()

class ArmiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armies
        fields = ['name']


from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    data_create = serializers.DateTimeField()
    data_updated = serializers.DateTimeField()
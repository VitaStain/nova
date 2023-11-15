from rest_framework import serializers


class GoogleDriveDocCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    data = serializers.CharField(max_length=None)

    def create(self, validated_data):
        return validated_data

from rest_framework import serializers

from apps.google_drive.services.google_drive import GoogleDriveService


# from apps.google_drive.tasks import create_file_in_google_drive


class GoogleDriveDocCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    data = serializers.CharField(max_length=None)

    def create(self, validated_data):
        # use celery if deploy services allow it

        # create_file_in_google_drive.apply_async(
        #     args=[validated_data["name"], validated_data["data"]]
        # )

        service = GoogleDriveService()
        service.create_text_file(validated_data["name"], validated_data["data"])

        return validated_data

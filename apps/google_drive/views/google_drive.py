from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.google_drive.serializers.google_drive import GoogleDriveDocCreateSerializer


@extend_schema(tags=["google_drive"])
@extend_schema_view(
    post=extend_schema(
        summary="Create a Google Drive Document",
        description="""
        Name - name of Google Drive Document
        Data - data of Google Drive Document
        """,
    )
)
class GoogleDriveDocCreateView(APIView):
    serializer_class = GoogleDriveDocCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

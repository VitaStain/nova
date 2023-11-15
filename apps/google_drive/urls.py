from django.urls import path, include

from apps.google_drive.views.google_drive import GoogleDriveDocCreateView

urlpatterns = [
    path(
        "v1/",
        include([
            path(
                "google_drive/docs/",
                GoogleDriveDocCreateView.as_view(),
            ),
        ]),
    )
]

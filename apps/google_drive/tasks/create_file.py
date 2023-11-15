from celery import shared_task

from apps.google_drive.services.google_drive import GoogleDriveService


@shared_task
def create_file_in_google_drive(name: str, data: str) -> None:
    """
    Create a text file in Google Drive
    """
    service = GoogleDriveService()
    service.create_text_file(name, data)

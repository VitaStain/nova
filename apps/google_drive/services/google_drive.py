import io
import os
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from oauth2client.service_account import ServiceAccountCredentials


class GoogleDriveService:
    def __init__(self):
        self._SCOPES = ["https://www.googleapis.com/auth/drive"]

        _base_path = os.path.dirname(__file__)
        _credential_path = Path("", "credential.json")
        self._credential_path = _credential_path

    def build(self):
        """
        Build Google Drive Service
        """
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            self._credential_path, self._SCOPES
        )
        service = build("drive", "v3", credentials=creds)

        return service

    def create_text_file(self, name: str, data: str) -> dict:
        """
        Create a text file in Google Drive
        """
        service = self.build()

        media_body = MediaIoBaseUpload(
            io.BytesIO(data.encode()), mimetype="text/plain", resumable=True
        )

        file_metadata = {
            "name": name,
            "mimeType": "text/plain",
            "parents": [folder.get("id") for folder in self.get_folders()],
        }

        file: dict = (
            service.files().create(body=file_metadata, media_body=media_body).execute()
        )

        return file

    def get_folders(self) -> list:
        """
        get all folders in Google Drive
        """

        service = self.build()
        results = (
            service.files()
            .list(
                q="mimeType='application/vnd.google-apps.folder'",
                fields="files(id, name)",
            )
            .execute()
        )

        folders = results.get("files", [])
        return folders

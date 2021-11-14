from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from os.path import exists, splitext
import uuid

class Uploader:
    def __init__(self):
        self._stubbed = False
        if exists("creds.json"):
            self._gauth = GoogleAuth()
            self._gauth.GetFlow()
            self._gauth.flow.params.update({"access_type": "offline"})
            self._gauth.LoadCredentialsFile("creds.json")
            self._gauth.Refresh()
            self._gdrive = GoogleDrive()
        elif exists("petitioner_app/templates/uploader/creds.json"):
            self._gauth = GoogleAuth()
            self._gauth.GetFlow()
            self._gauth.flow.params.update({"access_type": "offline"})
            self._gauth.LoadCredentialsFile("petitioner_app/templates/uploader/creds.json")
            self._gauth.Refresh()
            self._gdrive = GoogleDrive()
        else:
            print("Created a stubbed google drive uploader class. For GDrive support make sure to run the setup.py script.")

    def _generate_name(self, extension):
        return str(uuid.uuid4())+extension

    def upload(self, filepath):
        # returns a tuple of (id, filename) of the file on the gdrive itself
        name = self._generate_name(splitext(filepath)[1])
        if not self._stubbed:
            f = self._gdrive.CreateFile({"title": name})
            f.SetContentFile(filepath)
            f.Upload()
        return (id, name)

    def download(self, id_drive, file_local):
        # doesn't work yet
        if not self._stubbed:
            f = self._gdrive.CreateFile({"title": file_drive})
            f.GetContentFile(file_local)
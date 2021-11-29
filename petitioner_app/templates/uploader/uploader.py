from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from os.path import exists, splitext
import uuid

class Uploader:
    def __init__(self):
        self._stubbed = False
        if exists("creds.json"):
            self._gauth = GoogleAuth()
            self._gauth.LoadCredentialsFile("creds.json")
            self._gdrive = GoogleDrive()
        elif exists("petitioner_app/templates/uploader/creds.json"):
            self._gauth = GoogleAuth()
            self._gauth.LoadCredentialsFile("petitioner_app/templates/uploader/creds.json")
            self._gdrive = GoogleDrive()
        else:
            print("Created a stubbed google drive uploader class. For GDrive support make sure to run the setup.py script.")

    def _generate_name(self, extension):
        return str(uuid.uuid4())+extension

    def upload(self, filepath):
        # returns the id of the file on the gdrive itself
        name = self._generate_name(splitext(filepath)[1])
        if not self._stubbed:
            f = self._gdrive.CreateFile({"title": name})
            f.SetContentFile(filepath)
            f.Upload()
            # screw security, I just want to get it over with
            permission = f.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
            return f["id"]
        return None

    def download(self, id_drive, file_local):
        if not self._stubbed:
            f = self._gdrive.CreateFile({"id": id_drive})
            f.GetContentFile(file_local)

    def get_link(self, id_drive):
        if not self._stubbed:
            f = self._gdrive.CreateFile({"id": id_drive})
            f.FetchMetadata(fetch_all=True)
            return f['alternateLink']
        return None
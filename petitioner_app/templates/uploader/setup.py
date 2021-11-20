# before first run of this app you have to run the setup.py script
# to do so you need client_secrets.json from the google console to be able to access the API
# see the https://docs.iterative.ai/PyDrive2/quickstart/#authentication for details

from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()

gauth.LocalWebserverAuth()
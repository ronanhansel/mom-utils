from Google import create_service
import os
import json

API_NAME = 'drive'
API_VERSION = 'v3'
CLIENT_SECRET = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
DEFAULT_ID = input("Please input your folder ID, it's the sequence of gibberish at the end of your folder's url:\n")
service = create_service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)


def create(folder):
    folders = folder.split("/")
    folder_id = ''
    second_id = ''
    default_id = DEFAULT_ID
    for i in folders:
        if folder_id == '':
            folder_id = default_id
        if "|" in i:
            a = i.split("|")
            for e in a:
                if ">" in e:
                    if second_id == '': second_id = folder_id
                    c = e.split(">")
                    for m in c:
                        file_metadata = {
                                'name': m,
                                'mimeType': 'application/vnd.google-apps.folder',
                                'parents': [second_id]
                            }
                        file_second = service.files().create(body=file_metadata,
                                            supportsAllDrives=True, fields='id').execute()
                        second_id = file_second.get('id')
                        if m == c[-1]: second_id = folder_id
                else: 
                    file_metadata = {
                                    'name': e,
                                    'mimeType': 'application/vnd.google-apps.folder',
                                    'parents': [folder_id]
                                }
                    file_second = service.files().create(body=file_metadata,
                                        supportsAllDrives=True, fields='id').execute()
                    second_id = file_second.get('id')

            return
        else:
            file_metadata = {
                'name': i,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [folder_id]
            }
            file = service.files().create(body=file_metadata,
                                          supportsAllDrives=True, fields='id').execute()
            folder_id = file.get('id')

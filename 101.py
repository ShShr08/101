import dropbox
import time
import random

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '<access token>'
    transferData = TransferData(access_token)

    file_from = input('Enter file path to transfer : ')
    file_to = input('Enter path to upload to dropbox : ')
    transferData.upload_file(file_from, file_to)
    print('Moved')

if __name__ == '__main__':
    main()
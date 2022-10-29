from filestack import Client


class Fileshare:
    def __init__(self, filepath, api_key):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(str(self.api_key))

        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

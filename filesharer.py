import os
import webbrowser
from filestack import Client
from secret.filestack_apikey import API_KEY  # Import secret API key

class FileSharer:
    """
    Represents a Filestack API instance for uploading files and generating shareable links.

    Attributes:
        file_path (str): The path of the file to be uploaded.
        api_key (str): The API key for authenticating with the Filestack service.
    """

    def __init__(self, file_path, api_key=API_KEY):
        """
        Initializes the FileSharer with the given file path and API key.

        Args:
            file_path (str): The path of the file to be uploaded.
            api_key (str): The API key for Filestack (default is imported from secret).
        """
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        """
        Uploads the file to Filestack and returns the generated shareable link.

        Returns:
            str: The URL of the uploaded file.

        Raises:
            Exception: If the upload fails.
        """
        try:
            client = Client(self.api_key)  # Instantiate Filestack client
            new_filelink = client.upload(filepath=self.file_path)  # Upload file and get link
            return new_filelink.url  # Return link
        except Exception as e:
            raise Exception(f"An error occurred while uploading the file: {e}")

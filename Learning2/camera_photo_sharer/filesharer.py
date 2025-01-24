from filestack import Client

class FileSharer:
    """Filesharer for filestack file sharing
    """    
    def __init__(self, filepath : str, api_key : str):
        """Remember to provide the api key for connection
        Args:
            filepath (str): filepath for sharing
            api_key (str): api key
        """        #provide api key
        self.filepath = filepath
        self.api_key = api_key
        
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
import requests

class NewsFeed():
    """Class for getting news via newsapi
    """    
    
    def __init__(self, interest: str, search_for : str = "", from_date: str = "", to_date: str = "", language: str = "", sortBy : str = "" ):
        """Args:
            interest (str): topic
            search_for (str): title,description,content separated or together
            from_date (str): date from (2024-07-08)
            to_date (str): date to (2024-07-08)
            language (str): language ( 2-letter ISO-639-1)
            sortBy (str): relevancy, popularity, publishedAt (default)
        """      
        #I dont know if this is very bad Idea to have this many if else conditions in init
        # but its ran only once so maybe not too bad?
        self.nan = 'nan'
        self.base_url = "https://newsapi.org/v2/everything?"  
        self.interest = "q="+interest+"&"
        self.search_for = "searchIn="+search_for+"&" if not search_for == self.nan else ""
        self.from_date = "from="+ from_date +"&" if not from_date == self.nan else ""
        self.to_date =  "to=" + to_date + "&" if not to_date == self.nan else ""
        self.language =  "language="+ language + "&" if not language == self.nan else ""
        self.sortBy = "sortBy=" + sortBy + "&" if not sortBy == self.nan else ""
        self.api_key = "apiKey=putApiKeyHere" # REMEMBER TO DELETE THE API KEY FROM PUBLIC
        
    def get(self) -> str:
        """Makes a request based on constructed url request and 
        return a string contains search results by
        title and article url
        """        
        url = self.base_url + self.interest + self.search_for \
            + self.from_date + self.to_date + self.language \
            + self.sortBy + self.api_key
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body_text = ""
        for article in articles:
            email_body_text = email_body_text + article['title'] \
                + "\n" + article['url'] + "\n\n"
        return email_body_text

if __name__ == "__main__":
    interest = "bitcoin"
    search_result = NewsFeed(interest=interest, search_for="title",
                      from_date=None,
                      to_date=None,
                      language="en",
                      sortBy="popularity").get()
    
    print(search_result)
import requests as req
from selectorlib import Extractor


class Temperature():

    """Represents the temperature value extracteed from the timeanddate.com/.
    """   
     
    base_url_path = 'https://www.timeanddate.com/worldclock'
    yml_path = 'calorie_app/temperature.yaml'
    
    def __init__(self, country: str, city: str):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")
        
    def _build_url(self):
        """Builds the full url path
        """        
        return self.base_url_path + '/' + self.country + '/' + self.city
    
    def _scrape_data(self):
        """Tries to extract a value instructed 
        by yaml file and returns a dictionary
        """        
        try:
            url_page_request = req.get(self._build_url())
            extractor = Extractor.from_yaml_file(self.yml_path) 
            raw_data = extractor.extract(url_page_request.text)
            return raw_data
        except Exception as e:
            print(f"Error message: {e}")
            print("Either no country or city of that name exists - Please try again")
            
    def get(self):
        try:
            scraped_contents = self._scrape_data()
            scraped_contents = float(scraped_contents['temp'].replace("°C", "").strip())
            return scraped_contents
        except Exception as e:
            print(f"Error message: {e}")
            print(f"Failed to get the temperature data through {self.base_url_path}")
            print("*****")
            print("Setting temp as default 10°C ")
            return 10
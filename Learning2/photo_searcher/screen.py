from kivy.uix.screenmanager import Screen
import wikipediaapi  as wikipedia
import requests
import re

class FirstScreen(Screen):
    
    #Does not work porperly right now
    
    def search_image(self):

        def search_for_image_link(html_link):
            #I dont know how to properly search through the image for now
            pass
        
        # Get user text input 
        text_query = self.manager.current_screen.ids.text_id.text
        #Get wikipedia page and first image from the list of image urls
        wiki_instance = wikipedia.Wikipedia(user_agent="CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)")
        page = wiki_instance.page(text_query)#wiki_instance.page(text_query)
        if page.exists():
            image_link = page.fullurl
                # set up headers so wikipedia does not block the connection attempt, at least without this it doesnt work
            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
            #ask for the page of wikipedia provided by the link
            request_page = requests.get(image_link, headers)
            #seach for first image in text file
            first_image = search_for_image_link(request_page.text)
            if first_image:
                true_image_link = first_image
                request_image = requests.get(true_image_link, headers)
                filepath = 'photo_searcher/files/picture.png'
                with open(filepath, 'wb') as file:
                    file.write(request_image.content)
                    #Setting the image in the widget
                    self.manager.current_screen.ids.img_id.source = filepath
            else:
                print("No images were found for this page")
        else:
             print(f"The wikipedia page for query {text_query} does not exist")
             print(f"Please re-think entry query and try the search again")
    
class SecondScreen(Screen):
    
    def search_image(self):
        pass
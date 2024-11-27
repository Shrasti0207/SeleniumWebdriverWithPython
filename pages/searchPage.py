from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    url = 'https://duckduckgo.com/'
    Search_Input = (By.ID, 'searchbox_input')

    #Intializer
    def __init__(self, browser):
        self.browser = browser

    #Interact with url
    def load(self):
        self.browser.get(self.url)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.Search_Input)
        search_input.send_keys(phrase + Keys.RETURN)

    def title(self):
        return self.browser.title

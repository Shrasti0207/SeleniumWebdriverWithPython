from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class orangeHrmLoginPage():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    Username_Input = (By.CSS_SELECTOR, 'input[name="username"]')
    Password_Input = (By.CSS_SELECTOR, 'input[name="password"]')

    def __init__(self, browser):
        self.browser = browser

    #Interact with url
    def load(self):
        self.browser.get(self.url)

    def login(self, username, password):
       username_input = self.browser.find_element(*self.Username_Input)
       username_input.send_keys(username)
       password_input = self.browser.find_element(*self.Password_Input)
       password_input.send_keys(password + Keys.RETURN)
       




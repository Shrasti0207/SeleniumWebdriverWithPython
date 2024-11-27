import pytest
from pages.loginPage import orangeHrmLoginPage

def test_basic_search(browser):
    login_page = orangeHrmLoginPage(browser)

    username = "Admin"
    password = "admin123"

    login_page.load()

    login_page.login(username, password)

import pytest
from pages.searchPage import DuckDuckGoSearchPage

def test_basic_search(browser):
    search_page = DuckDuckGoSearchPage(browser)

    phrase = "panda"

    search_page.load()

    search_page.search(phrase)

    assert phrase in search_page.title()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from playwright.sync_api import sync_playwright
import pytest
from pages.LoginPage import Login

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
        
"""@pytest.fixture
def loggedinpage(page):
    l = Login(page)
    l.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")
    return page
"""

import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.LoginPage import Login

@pytest.mark.skip(reason="Login test not required in normal runs")
def test_LoginPage(page):
    l = Login(page)
    l.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")

    
    
   
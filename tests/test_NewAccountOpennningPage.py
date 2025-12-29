import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.LoginPage import Login
from pages.NewAccountOpenningPage import NewAccountOpenningPage

@pytest.mark.skip
def test_NewAccountOpennningPage(page):
    l = Login(page)
    l.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")
    ac_no = NewAccountOpenningPage(page)
    ac_no.acc_creation()

    
    
   
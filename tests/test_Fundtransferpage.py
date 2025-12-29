import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from pages.Fundtransferpage import Fundtransferpage
from pages.Fundtransferpage import Fundtransferpage
from pages.LoginPage import Login
from pages.NewAccountOpenningPage import NewAccountOpenningPage
import pytest


#@pytest.mark.skip(reason="Login test not required in normal runs")
def test_NewAccountOpennningPage(page):
    l = Login(page)
    l.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")
    ac_no = NewAccountOpenningPage(page)
    accno=ac_no.acc_creation()
    #ft = Fundtransferpage(5000, 12345, accno )
    #ft.Fundtransfer()
    ft = Fundtransferpage(page)
    ft.Fundtransfer(amount=5000, toacc=accno)

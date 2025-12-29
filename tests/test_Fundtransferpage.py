import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from pages.Fundtransferpage import Fundtransferpage
from pages.Fundtransferpage import Fundtransferpage
from pages.LoginPage import Login
from pages.NewAccountOpenningPage import NewAccountOpenningPage


def test_NewAccountOpennningPage(loggedinpage):
    #l = Login(page)
    #l.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")
    ac_no = NewAccountOpenningPage(loggedinpage)
    accno=ac_no.acc_creation()
    #ft = Fundtransferpage(5000, 12345, accno )
    #ft.Fundtransfer()
    ft = Fundtransferpage(loggedinpage)
    ft.fund_transfer(amount=5000, from_acc=None, to_acc=accno)


import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))    

class Login():
    def __init__(self, page):
        self.page = page

    def verify_login(self,url,usrnm,pswrd):
        self.page.goto(url)
        self.page.fill("//*[@name='username']",usrnm)
        self. page.fill("//*[@name='password']",pswrd)
        self.page.click("//*[@type='submit']")
        assert "ParaBank | Accounts Overview" == (self.page.title())

    

    




import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  
from pages.LoginPage import Login  

class NewAccountOpenningPage():
    def __init__(self, page):
        self.page = page
        #self.v= Login(page)

    def acc_creation(self):
        #self.v.verify_login("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC","john","demo")
        self.page.click("//*[text()='Open New Account']")
        self.page.click("//*[@id='type']")
        self.page.locator("//*[@id='type']").select_option(index=1)
        self.page.locator("//*[@id='fromAccountId']").select_option(value='12345')
        self.page.click("((//*[@class='button'])[2])")
        self.page.locator("//*[@id='newAccountId']").wait_for(state="visible")
        acc_num=self.page.locator("//*[@id='newAccountId']").text_content().strip()
        print("acc_num:",acc_num)

        head ={"Accept": "application/xml"}
        response = requests.get(f"https://parabank.parasoft.com/parabank/services/bank/accounts/{acc_num}", headers = head  )
        print(response.status_code)
        assert 200 == response.status_code
        print("response text:",response.text)
        assert acc_num in response.text
        return acc_num

        


        

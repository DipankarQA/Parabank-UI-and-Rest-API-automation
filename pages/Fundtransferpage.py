from pages.NewAccountOpenningPage import NewAccountOpenningPage
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class Fundtransferpage():
    def __init__(self, page):
        self.page = page
        #self.f=NewAccountOpenningPage(page)
        #toacc =self.f.acc_creation(page)
    def Fundtransfer(self, amount, toacc ):
        self.page.locator("//*[text()='Transfer Funds']").click()
        
        self.page.locator("//*[@id='amount']").fill(str(amount))
        
        self.page.locator("//*[@id='fromAccountId']").select_option(value="12345")
        
        self.page.locator("//*[@id='toAccountId']").select_option(value = toacc)
        
        self.page.locator("//*[@value='Transfer']").click()
        
        successtext=(self.page.locator("//*[text()='Transfer Complete!']").text_content())
        print(successtext)
        head ={"Accept": "application/xml"}
        response = requests.get(f"https://parabank.parasoft.com/parabank/services/bank/accounts/{toacc}",
                                 headers = head  )
        print(response.status_code)
        assert 200 == response.status_code
        print("response text:",response.text)
        assert toacc in response.text
        return toacc


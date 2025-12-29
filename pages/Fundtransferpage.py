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
    def Fundtransfer(self, amount, fromacc, toacc ):
        self.page.locator("//*[text()='Transfer Funds']").click()
        self.page.locator("//*[@id='amount']").fill(str(amount))
        """fromacc="12345"
        self.page.locator("//*[@id='fromAccountId']").select_option(value=fromacc)
        self.page.locator("//*[@id='toAccountId']").select_option(value = toacc)"""
        self.page.wait_for_selector("#fromAccountId option")
        self.page.locator("#fromAccountId").select_option(index=0)

        self.page.wait_for_selector("#toAccountId option")
        self.page.locator("#toAccountId").select_option(value=str(toacc))

        self.page.locator("//*[@value='Transfer']").click()
        successtext=(self.page.locator("//*[text()='Transfer Complete!']").text_content())
        print(successtext)
        head ={"Accept": "application/xml"}
        response = requests.get(f"https://parabank.parasoft.com/parabank/services/bank/accounts/{toacc}",
                                 headers = head  )
        print(response.status_code)
        assert 200 == response.status_code
        print("response text:",response.text)
        #assert toacc in response.text
        return toacc


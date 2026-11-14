import time
from playwright.sync_api import Page

def test_loginCheck(page:Page):
    page.goto("https://rahulshettyacademy.com/sign_in/")
    time.sleep(2)
    page.get_by_label("Email Address").fill("infobasu96@gmail.com")
    page.get_by_label("Password").fill("dataSet")
    time.sleep(2)
    page.locator("//input[@value='Log In']").click()
    
    

    
from playwright.sync_api import Page ,sync_playwright,expect

def verifyPageTitle(page:Page):
    page.goto("https://www.google.com")
    print(page.title())
    

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    verifyPageTitle(page)
    browser.close()
from playwright.async_api import Playwright,Page

def  test_browser_launch(playwright:Playwright,page:Page):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page() 
    page.goto("https://www.w3schools.com")
    page.goto("https://google.com")
    
 
def  test_new_browser_page(page:Page):                                                                                                                      
    page.goto("https://www.google.com")
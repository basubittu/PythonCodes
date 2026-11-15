from playwright.sync_api import Playwright
def test_loginCheck_new(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page= context.new_page()
    page.goto("https://www.w3schools.com")
    page.screenshot(path="C:\\pythonData\\PythonCodes\\DataCheck\\data_new1.png")
    
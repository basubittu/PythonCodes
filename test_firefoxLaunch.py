from playwright.sync_api import Playwright
def test_launchFirfoxbrowser(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.w3schools.com")
    page.screenshot(path="data.png")
    
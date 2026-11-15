import time
from playwright.sync_api import Page,expect
def test_loginPage(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//input[@id='name']").fill("Abhishek Basu")
    page.locator("//input[@id='email']").fill("infobasu96@gmail.com")
    page.locator("//input[@id='phone']").fill("9635233630")
    page.locator("//textarea[@id='textarea']").fill("Abcdefgh")
    
    page.locator("//label[text()='Male']/preceding-sibling::input").click()
    time.sleep(2)
    page.locator("//label[text()='Tuesday']/preceding-sibling::input").click()
    time.sleep(5)
    page.get_by_role("combobox").select_option("uk")
    time.sleep(5)
    page.locator("//select[@id='colors']").select_option("green")
    time.sleep(2)
    page.locator("//select[@id='animals']").select_option("lion")
    time.sleep(2)
    page.locator("#datepicker").click()
    page.locator("//a[text()='14']").click()
    time.sleep(2)
    page.locator("//input[@name='SelectedDate']").click()
    page.locator("//a[text()='17']").click()
    time.sleep(2)
    expect(page.get_by_text("Data Entry Form")).to_be_visible()
   
    
    
    
    
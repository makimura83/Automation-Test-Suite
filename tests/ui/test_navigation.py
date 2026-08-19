from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_home_page_loads(browser):
    assert "Google" in browser.title

def test_search_on_google(browser):
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Robot Framework")
    search_box.send_keys(Keys.RETURN)
    
    # รอผลลัพธ์ขึ้นนิดหน่อย
    browser.implicitly_wait(3)
    assert "Robot Framework" in browser.page_source
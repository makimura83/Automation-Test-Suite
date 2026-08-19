from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search_box_exists(browser):
    search_box = browser.find_element(By.NAME, "q")
    assert search_box.is_displayed()

def test_google_logo_exists(browser):
    # ใช้ selector ที่เสถียรกว่า
    logo = browser.find_element(By.CSS_SELECTOR, "img[alt='Google'], img[id='hplogo'], svg[aria-label='Google']")
    assert logo.is_displayed()
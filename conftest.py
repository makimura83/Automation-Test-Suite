import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://api.jikan.moe/v4"
UI_URL = "https://www.google.com"   # เปลี่ยนเป็น URL จริงของคุณ

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(UI_URL)
    yield driver
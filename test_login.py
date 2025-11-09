from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

def test_login_valid(setup):
    driver = setup
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login").click()
    assert "Dashboard" in driver.title

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    yield driver
    driver.quit()

def test_navigation(setup):
    driver = setup
    driver.find_element(By.LINK_TEXT, "About").click()
    assert "About Us" in driver.title

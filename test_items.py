import pytest
from selenium.webdriver.common.by import By


def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        return True
    except:
        return False

class TestForButtons():
    def test_checkbutton(self, browser):
        assert is_element_present(browser)== True, "корзинка не найдена"


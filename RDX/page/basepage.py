from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None):
        if self._driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9333"
            self._driver = webdriver.Chrome()
            # self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_to_click(self, time, locator):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

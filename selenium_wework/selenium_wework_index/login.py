from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, '#menu_contacts .frame_nav_item_title').click()
        return True


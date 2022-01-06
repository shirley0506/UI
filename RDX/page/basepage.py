import inspect

import yaml
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
        self._driver = driver

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def send_keys(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def wait_to_click(self, time, locator):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == step["action"]:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "finds" == step["action"]:
                    # eles = self.finds(step["by"], step["locator"])
                    if 'subaction' in step.keys():
                        self.combobox(step["by"], step["locator"], step["value"], step["subaction"])
                    else:
                        self.combobox(step["by"], step["locator"], step["value"])
                if "text" == step["action"]:
                    return self.find(step["by"], step["locator"]).text == step["value"]

    def combobox(self, by, locator, value, subaction=None):
        eles = self.finds(by, locator)
        for ele in eles:
            if ele.text == value:
                if subaction == 'move':
                    from selenium.webdriver import ActionChains
                    ActionChains(self._driver).move_to_element(ele).perform()
                else:
                    ele.click()
            if ele.get_attribute('value') == value:
                ele.click()

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework.selenium_wework_main.page.basepage import BasePage


class AddMember(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self._driver = driver

    def add_member(self):
        sleep(2)
        self.find(By.ID, "username").send_keys("test")
        self.find(By.ID, "memberAdd_acctid").send_keys("test")
        self.find(By.ID, "memberAdd_phone").send_keys("12345678901")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_members(self):
        sleep(2)
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        return [element.get_attribute('title') for element in elements]


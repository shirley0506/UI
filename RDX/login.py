#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium import webdriver

from RDX.index import Index
from RDX.page.basepage import BasePage


class Login(BasePage):
    _base_url = "http://172.20.3.43:3600/login"
    # def __init__(self):
    #     self._driver = webdriver.Chrome()
    #     self._driver.get("http://172.20.3.43:3600/login")

    def login(self):
        # click username、password
        self.wait_to_click(10, (By.ID, "name"))
        self.find(By.ID, "name").send_keys("admin")
        self.find(By.ID, "password").send_keys("123123")
        self.find(By.CSS_SELECTOR, ".login-submit-btn").click()
        return Index(self._driver)

    def logout(self):
        self._driver.close()


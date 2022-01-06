#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from selenium.webdriver.common.by import By
from selenium import webdriver

from RDX.page.main import Main
from RDX.page.basepage import BasePage


class Login(BasePage):

    def __init__(self):
        # 对驱动初始化
        self._base_url = "http://172.20.3.43:3600/login"
        self._driver = webdriver.Chrome()
        self._driver.get(self._base_url)
        # self._driver.maximize_window()
        self._driver.implicitly_wait(10)

    def login(self) -> Main:
        self.steps("/Users/shirleyxu/Documents/Python/UI/RDX/page/login.yaml")
        # self.find(By.ID, "name").send_keys("admin")
        # self.find(By.ID, "password").send_keys("123123")
        # self.find(By.CSS_SELECTOR, ".login-submit-btn").click()
        return Main(self._driver)

    def logout(self):
        self._driver.close()

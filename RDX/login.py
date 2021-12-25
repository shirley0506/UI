#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium import webdriver

from RDX.index import Index


class Login:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("http://172.20.3.43:3600/login")

    def login(self):
        # click username、password
        self._driver.find_element(By.ID, "name").send_keys("admin")
        self._driver.find_element(By.ID, "password").send_keys("123123")
        self._driver.find_element(By.CSS_SELECTOR, ".login-submit-btn").click()
        return Index(self._driver)


#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Dataportal:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_Project(self, projectName, description):
        self._driver.find_element(By.CSS_SELECTOR, ".anticon-plus").click()
        self._driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(projectName)
        self._driver.find_element(By.XPATH, '//*[@id="description"]').send_keys(description)
        self._driver.find_element(By.XPATH, "//*[@class='ant-modal-footer']/button").click()
        return self.add_Api

    def add_Api(self):
        pass
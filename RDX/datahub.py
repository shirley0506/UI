#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver


class DataHub:
    def __init__(self, driver: WebDriver):
        self._driver = driver
    pass

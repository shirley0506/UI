#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from RDX.datahub import DataHub
from RDX.dataportal import Dataportal
from RDX.datasource import DataSource


class Index:
    def __init__(self, driver):
        '''
        options = Options()
        options.debugger_address = "127.0.0.1:9333"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get("https://work.weixin.qq.com/")
        '''
        self._driver = driver

    def goto_datahub(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return DataHub(self._driver)

    def goto_datasource(self):
        return DataSource(self._driver)

    def goto_dataportal(self):
        self._driver.find_element(By.LINK_TEXT, "数据服务").click()
        return Dataportal(self._driver)

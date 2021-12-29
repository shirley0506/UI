#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from RDX.datahub import DataHub
from RDX.dataportal import Dataportal
from RDX.datasource import DataSource
from RDX.page.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class Index(BasePage):
    _base_url = 'http://172.20.3.43:3600/login'

    def __init__(self, driver):
        #     '''
        #     options = Options()
        #     options.debugger_address = "127.0.0.1:9333"
        #     self._driver = webdriver.Chrome(options=options)
        #     self._driver.get("https://work.weixin.qq.com/")
        #     '''
        self._driver = driver

    def goto_datahub(self):
        self.wait_to_click(10, (By.CSS_SELECTOR, '.index_top_operation_loginBtn'))
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return DataHub(self._driver)

    def goto_datasource(self):
        self.wait_to_click(10, (By.CSS_SELECTOR, '.ant-dropdown-trigger>a'))
        tabs = self.finds(By.CSS_SELECTOR, '.ant-dropdown-trigger>a')
        for tab in tabs:
            if tab.text == '数据资产':
                ActionChains(self._driver).move_to_element(tab).perform()
                subtabs = self.finds(By.CSS_SELECTOR, '.ant-dropdown-menu-item>a')
                for subtab in subtabs:
                    if subtab.text == '数据源资产':
                        # self.wait_to_click(10, (By.CSS_SELECTOR, '.rt-submenu-active'))
                        # self.find(By.CSS_SELECTOR, '.rt-submenu-active').click()
                        subtab.click()
                        return DataSource(self._driver)


    def goto_dataportal(self):
        self.find(By.LINK_TEXT, "数据服务").click()
        return Dataportal(self._driver)

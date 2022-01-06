#!/usr/bin/python3
# -*- coding: utf-8 -*-
import inspect
from time import sleep

import yaml
from selenium.webdriver.common.by import By
from selenium import webdriver
from RDX.page.basepage import BasePage


class DataSource(BasePage):
    # def __init__(self, driver):
    #     self._driver = driver

    def add_source(self):
        self.steps('/Users/shirleyxu/Documents/Python/UI/RDX/page/datasource1.yaml')
        # self.find(By.XPATH, "//div[@class='ant-modal-footer']/div/button/span[text()='测试连接']").click()
        # self.find(By.XPATH, '//div[contains(@class,"ant-modal-footer")]/div/button[1]').click()
        # self.find(By.XPATH, '//div[contains(@class,"ant-modal-footer")]/div/button[3]').click()

        # self.wait_to_click(10, (By.CSS_SELECTOR, '.ant-btn-primary'))
        # self.find(By.CSS_SELECTOR, '.ant-btn-primary').click()
        # self.find(By.ID, 'base_name').send_keys('test')
        # self.find(By.ID, 'datasourceType').click()
        # datatypes = self.finds(By.CSS_SELECTOR, '.ant-select-dropdown-menu-vertical li')
        # for datatype in datatypes:
        #     if datatype.text == 'mysql':
        #         datatype.click()
        #         break
        # self.find(By.ID, 'datasourceVersion').click()
        # versions = self.finds(By.CSS_SELECTOR, '.ant-select-dropdown-menu-vertical li')
        # for version in versions:
        #     if version.text == 'v8':
        #         version.click()
        #         break
        # checkboxs = self.finds(By.CSS_SELECTOR, '.ant-checkbox-input')
        # for checkbox in checkboxs:
        #     if checkbox.get_attribute('value') == 'isEnableApiSource':
        #         checkbox.click()
        #         break
        # self.find(By.CSS_SELECTOR, '.ant-modal-footer .ant-btn-primary').click()
        # self.wait_to_click(10, (By.ID, 'url'))
        # self.find((By.ID, 'url')).send_keys('jdbc:mysql://172.20.3.43:3307/dataportal')
        # self.find(By.ID, 'username').send_keys('dcuser')
        # self.send_keys(By.ID, 'username', 'dcuser')
        # self.find(By.ID, 'password').send_keys('DataCanvas!23')
        # self.send_keys(By.ID, 'password', 'DataCanvas!23')
        # self.find(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/button[1]').click()
        # self.find(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/button[3]').click()
        # buttons = self.finds(By.CSS_SELECTOR, '.ant-modal-footer button')
        # for button in buttons:
        #     if button.find_element(By.TAG_NAME, 'span').text == '测试连接':
        #         button.click()
        #     if button.find_element(By.TAG_NAME, 'span').text == '确定':
        #         button.click()

    def get_datasource(self, value):
        total_rows = self.find(By.CSS_SELECTOR, '.ant-pagination-total-text').text.split(' ')[1]
        self.find(By.CSS_SELECTOR, '.ant-select-selection-selected-value').click()
        # 先获取要点击的元素的文本，然后再点击
        page_rows = self.find(By.CSS_SELECTOR, '.ant-select-dropdown-menu-vertical>li:nth-last-child(1)').text.split()[0]
        self.find(By.CSS_SELECTOR, '.ant-select-dropdown-menu-vertical>li:nth-last-child(1)').click()
        # 获取总页数，既点击下一页的次数，判断预期值是不是在当前页，不在就点击下一页按钮
        pages = int(total_rows) // int(page_rows)
        count = 0
        while True:
            # 先判断当前页有没有预期值
            rows = self.finds(By.CSS_SELECTOR, '.ant-table-row-level-0>td:nth-child(2) a')
            for row in rows:
                if row.text == value:
                    return True
            # 判断翻页的次数是不是总次数，来预判当前页是不是最后一页。如果是最后一页，上面的循环也执行结束，说明整个列表页都没有预期值
            if count == pages:
                return False
            self.find(By.CSS_SELECTOR, '.ant-pagination-next').click()
            count += 1




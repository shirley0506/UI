from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wework.selenium_wework_index.login import Login
from selenium_wework.selenium_wework_index.register import Register


class Index:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9333"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self._driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

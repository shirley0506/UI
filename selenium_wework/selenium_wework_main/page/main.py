from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wework.selenium_wework_main.page.addmember import AddMember


class Main:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9333"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_add_member(self):
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap[node-type='addmember']").click()
        return AddMember(self._driver)



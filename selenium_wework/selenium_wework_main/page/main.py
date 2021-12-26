from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework.selenium_wework_main.page.addmember import AddMember
from selenium_wework.selenium_wework_main.page.basepage import BasePage


# Main继承PageBase，在被实例化时，会自动执行父类中的构造方法
# 既__init__方法，实现初始化driver的功能
from selenium_wework.selenium_wework_main.page.delmember import DelMember


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9333"
    #     self._driver = webdriver.Chrome(options=options)
    #     self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_add_member(self):
        """
        写了2个添加成员入口的方法
        :return: 调用AddMember函数
        """
        # 首页下发的添加成员入口
        # self._driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap[node-type='addmember']").click()
        # 首页上方通讯录-添加成员入口
        # 封装self._driver.find_element， 调用父类的函数用----self.函数名
        self.find(By.CSS_SELECTOR, '#menu_contacts>.frame_nav_item_title').click()
        # 显示等待，等待添加用户按钮可被点击
        self.wait_to_click(10, (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)

    def goto_del_member(self):
        """
        进入通讯录tab页，选择记录，删除
        :return: 调用DelMember函数
        """
        self.find(By.CSS_SELECTOR, '#menu_contacts>.frame_nav_item_title').click()
        self.wait_to_click(10, (By.CSS_SELECTOR, '.ww_checkbox'))
        return DelMember(self._driver)

from selenium.webdriver.common.by import By

from selenium_wework.selenium_wework_main.page.basepage import BasePage


class DelMember(BasePage):

    def del_member(self):
        self.wait_to_click(10, (By.CSS_SELECTOR, '.ww_checkbox'))
        names = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
        for name in names:
            if name.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').get_attribute('title') == 'test':
                name.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').click()
                self.find(By.CSS_SELECTOR, '.js_delete').click()
                self.wait_to_click(10, (By.CSS_SELECTOR, '.ww_dialog'))
                self.find(By.CSS_SELECTOR, '#__dialog__MNDialog__>div:nth-child(1)>div:nth-child(3)>a:nth-child(1)').click()


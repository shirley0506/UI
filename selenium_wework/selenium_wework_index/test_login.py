from selenium_wework.selenium_wework_index.index import Index
from selenium_wework.selenium_wework_index.login import Login


class TestLogin:
    def setup(self):
        self.login = Index()

    def test_login(self):
        assert self.login.goto_login().login()

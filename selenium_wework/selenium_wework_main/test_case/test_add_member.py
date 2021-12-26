import pytest

from selenium_wework.selenium_wework_main.page.main import Main


class Test_AddMember:
    def setup(self):
        self.main = Main()

    @pytest.mark.skip
    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        members = add_member.get_members()
        assert 'test' in members

    def test_del_member(self):
        self.main.goto_del_member().del_member()

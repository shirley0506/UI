from selenium_wework.selenium_wework_main.page.main import Main


class Test_AddMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        members = add_member.get_members()
        assert 'test' in members


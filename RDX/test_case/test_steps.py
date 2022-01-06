from login import Login


class TestSteps:
    def setup(self):
        self.login = Login()

    def test_add_datasource1(self):
        self.login.login().goto_datasource().add_source()

    def teardown(self):
        self.login.logout()



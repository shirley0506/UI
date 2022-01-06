import pytest

from RDX.page.login import Login


class Test_add_datasource:

    def setup(self):
        # self.index = Index()
        self.login = Login()

    @pytest.mark.skip
    def test_add_datasource(self):
        self.login.login().goto_datasource().add_mysql_source()

    def test_get_datasource(self):
        # self.login.login().goto_datasource().get_datasource('kafka_dnntest')
        self.login.login().goto_datasource()

    def teardown(self):
        self.login.logout()

import pytest

from RDX.login import Login
from index import Index


class Test_add_datasource:

    def setup(self):
        # self.index = Index()
        self.login = Login()

    @pytest.mark.skip
    def test_add_datasource(self):
        self.login.login().goto_datasource().add_mysql_source()

    def test_get_datasource(self):
        self.login.login().goto_datasource().get_datasource('kafka_dnntest')

    def teardown(self):
        self.login.logout()

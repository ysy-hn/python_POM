import unittest

from selenium import webdriver
from ddt import ddt, file_data
from login_page import LoginPage
from index_page import IndexPage
from time import sleep


@ddt
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()

    @file_data('../data/data.yaml')
    def test_1_login(self, account, password):
        self.lp.login(account, password)

    @file_data('../data/search.yaml')
    def test_1_login(self, txt):
        self.ip.search(txt)
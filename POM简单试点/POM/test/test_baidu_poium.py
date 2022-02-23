from time import sleep
from page.poium_baidu_page import BaiduPagePoium
from selenium import webdriver
import unittest


class TestBaiduPoium(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_baidu_search_case_poium(self):
        page = BaiduPagePoium(self.driver)
        page.get('http://www.baidu.com')
        page.search_input = 'selenium'
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title, 'selenium_百度搜索')



import unittest
from page.baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):

    # unittest增加全局变量，需要增加父类和子类
    # def __init__(self, methodName='runTest'):
    #     super(TestBaidu, self).__init__(methodName)

    page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.page = BaiduPage('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.quit_browser()

    def test_baidu_case(self):
        self.page.open_url('http://www.baidu.com')
        self.page.baidu('乔峰')
        self.page.sleep_time(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)

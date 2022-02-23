from basecase.base1 import BasePage


class BaiduPage(BasePage):
    """百度Page层， 百度页面封装操作到的元素"""
    def baidu(self, search_key):
        self.input_element('id', 'kw', search_key)
        self.click_element('id', 'su')


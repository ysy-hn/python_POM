from selenium.webdriver.common.by import By

from base_page import BasePage


class IndexPage(BasePage):
    url1 = 'url'
    input_el = (By.ID, '')
    button = (By.ID, '')

    def search(self, txt, ):
        self.visit(self.url1)
        self.input_(self.input_el, txt)
        self.click(self.button)

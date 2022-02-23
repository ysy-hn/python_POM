from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    url2 = ''
    user = (By.ID, '')
    pwd = (By.ID, '')
    button = (By.ID, '')

    def login(self, account, password):
        self.visit(self.url2)
        self.input_(self.user, account)
        self.input_(self.pwd, password)
        self.click(self.button)


if __name__ == '__main__':
    pass

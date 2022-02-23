class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser, link):

        self.browser = browser
        self.link = link

    def setup(self):

        self.browser.get(self.link)

    def is_element_displayed(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_not_displayed(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

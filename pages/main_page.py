import random

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def add_children(self):
        count_children = random.randint(2, 6)
        self.browser.find_element(*MainPageLocators.GUESTS_COUNTER_FIELD).click()
        for _ in range(count_children):
            self.browser.find_element(*MainPageLocators.ADD_CHILD_BTN).click()

        input_fields = self.browser.find_elements(*MainPageLocators.AGE_DROP_DOWN)
        assert len(input_fields) == count_children, "The number of age inputs isn't equal to number of added children"

    def choose_city(self):
        self.browser.find_element(*MainPageLocators.FIELD).click()
        self.browser.find_element(*MainPageLocators.CITY_FIELD).click()
        self.browser.find_element(*MainPageLocators.SEARCH_BTN).click()
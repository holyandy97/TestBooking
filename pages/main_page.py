import random

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """
    Class with methods for Main page(descendant of the BasePage class)
    """

    def should_add_children(self):
        """
        Method with checking that the number of age inputs isn't equal to number of added child's
        """
        count_children = random.randint(2, 6)
        self.browser.find_element(*MainPageLocators.GUESTS_COUNTER_FIELD).click()
        for _ in range(count_children):
            self.browser.find_element(*MainPageLocators.ADD_CHILD_BTN).click()

        ages_inputs = self.browser.find_elements(*MainPageLocators.AGE_DROP_DOWN)
        assert len(ages_inputs) == count_children, "The number of age inputs isn't equal to number of added child's"

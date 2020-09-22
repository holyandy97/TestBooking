from pages.locators import SearchPageLocators
from .base_page import BasePage


class ResultsPage(BasePage):

    # Verify that each result entry has booking price or banner saying no free places
    def check_booking_prices(self):
        self.browser.find_element(*SearchPageLocators.SHOW_BTN).click()
        self.browser.find_element(*SearchPageLocators.CHECK_OUT_DATE).click()
        self.browser.find_element(*SearchPageLocators.SEARCH_BTN).click()
        booking_prise_status = self.browser.find_elements(*SearchPageLocators.BOOKING_PRICE_OR_STATUS)
        results_items = self.browser.find_elements(*SearchPageLocators.RESULTS_ITEM)
        assert len(booking_prise_status) == len(results_items), \
            "result entry has not booking price or banner saying no free places"

    def is_calendar_opened(self):
        assert self.is_element_displayed(*SearchPageLocators.CALENDAR), \
            "The calendar isn't displayed after opening result page"

    # Verify that page with listed hotels is opened
    def is_hotels_listed(self):
        assert self.is_element_displayed(*SearchPageLocators.HOTEL_LIST), \
            "Listed hotels aren't displayed after opening result page"

    def price_or_status_are_not_displayed(self):
        assert self.is_element_not_displayed(*SearchPageLocators.BOOKING_PRICE_OR_STATUS), \
            "Booking price or status is displayed after opening result page"

    def calendar_opened_after_show_btn(self):
        self.browser.find_element(*SearchPageLocators.SHOW_BTN).click()
        assert self.is_element_displayed(*SearchPageLocators.CALENDAR), \
            "The calendar is not displayed after clicking the 'Show' button"
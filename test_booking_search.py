from pages.main_page import MainPage
from pages.results_page import ResultsPage


class TestBookingData():

    """
    Scenario 2. User is required to specify booking date to see booking price
        Preconditions: User is at home page
        1. choose any city from the menu below
        Expect:
        - page with listed hotels is opened
        - calendar for specifying check in date is opened
        - no result entry containing booking price or booking status
        2. Click "show prices" button for any hotel
        Expect:
        - calendar for specifying check in date is opened
        3. Set any dates for check in and out
        4. Submit search form
        Expect:
        - each result entry has booking price or banner saying no free places
        """

    def test_user(self, browser):
        link = "https://www.booking.com/"
        mp = MainPage(browser, link)
        mp.setup()
        mp.choose_city()
        result_page = ResultsPage(browser, browser.current_url)
        result_page.is_hotels_listed()
        result_page.is_calendar_opened()
        result_page.price_or_status_are_not_displayed()
        result_page.calendar_opened_after_show_btn()
        result_page.check_booking_prices()
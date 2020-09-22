from pages.main_page import MainPage


class TestSpecifyingChildrenAge():
    """
    Scenario 1. User is able to specify age of each child
        1. go to home page
        2. open menu for selecting strangers number
        3. specify N number of children (N > 1)
    Expect: the number of age inputs is equal to N
    """

    def test_specifying_children_age(self, browser):
        link = "https://www.booking.com/"
        mp = MainPage(browser, link)
        mp.setup()
        mp.add_children()
        mp.choose_city()

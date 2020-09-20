from pages.main_page import MainPage


class TestUserIsAbleToSpecifyAgeOfEachChild():

    def test_user_should_be_able_to_specify_age_of_each_child(self, browser):
        """
        Test scenario 1
        :param browser: driver instance
        """
        link = "https://www.booking.com/"
        mp = MainPage(browser, link)
        mp.open()
        mp.should_add_children()

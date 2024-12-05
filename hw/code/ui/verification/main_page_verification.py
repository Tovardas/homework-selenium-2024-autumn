class MainPageVerification:
    def __init__(self, main_page):
        self.main_page = main_page

    def check_slide_title_changed(self, initial_title):
        assert initial_title != self.main_page.get_slide_title()

    def check_url_opened(self, expected_url):
        assert self.main_page.driver.current_url == expected_url

    def check_case_title_in_page(self, case_title):
        print(case_title)
        print(self.main_page.get_title())
        assert case_title in self.main_page.get_title()
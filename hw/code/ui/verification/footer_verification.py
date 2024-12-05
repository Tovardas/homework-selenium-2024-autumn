class FooterVerification:
    def __init__(self, main_page):
        self.main_page = main_page

    def check_url_opened(self, expected_url):
        assert self.main_page.driver.current_url == expected_url

    def check_selected_language(self, expected_language):
        assert self.main_page.get_selected_language_from_footer() == expected_language
class PartnerPageVerification:
    def __init__(self, partner_page):
        self.partner_page = partner_page

    def check_url_opened(self, expected_url):
        assert self.partner_page.driver.current_url == expected_url

    def check_page_contains_formats(self, expected_formats):
        assert self.partner_page.page_contain_formats(expected_formats)

    def check_submit_button_disabled(self):
        assert self.partner_page.submit_button_is_disabled()

    def check_submit_button_enabled(self):
        assert not self.partner_page.submit_button_is_disabled()

    def check_submit_message_visible(self):
        assert self.partner_page.submit_message_became_visible()
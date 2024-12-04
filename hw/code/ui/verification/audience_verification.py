class AudienceVerification:
    def __init__(self, audience_page):
        self.audience_page = audience_page

    def check_create_audience_modal_elements(self):
        assert self.audience_page.create_audience_modal_page_became_visible()
        assert self.audience_page.audience_name_input_became_visible()
        assert self.audience_page.sidebar_sign_became_visible()
        assert self.audience_page.add_source_button_became_visible()
        assert self.audience_page.footer_buttons_became_visible()
        assert self.audience_page.cross_button_became_visible()

    def check_add_source_modal_elements(self):
        assert self.audience_page.add_source_modal_page_became_visible()
        assert self.audience_page.source_items_became_visible()

    def check_error_message(self, expected_error):
        assert self.audience_page.get_error() == expected_error

    def check_audience_created(self, expected_name):
        assert self.audience_page.get_created_audience_title() == expected_name

    def check_audience_deleted(self):
        assert self.audience_page.audience_item_became_invisible()

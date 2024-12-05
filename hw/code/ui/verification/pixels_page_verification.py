class PixelsPageVerification:
    def __init__(self, pixels_page):
        self.pixels_page = pixels_page

    def check_pixel_modal_visible(self):
        assert self.pixels_page.pixel_modal_became_visible()

    def check_pixel_domain_error(self):
        assert self.pixels_page.pixel_domain_error_displayed()

    def check_pixel_email_error(self):
        assert self.pixels_page.pixel_email_error_displayed()

    def check_pixel_creation_success(self):
        assert self.pixels_page.pixel_creation_success()

    def check_tag_name_field_error(self):
        assert self.pixels_page.tag_name_field_error()

    def check_new_tag_displayed(self):
        assert self.pixels_page.new_tag_is_displayed()

    def check_event_url_field_displayed(self):
        assert self.pixels_page.event_url_field_is_displayed()

    def check_event_set_value_field_displayed(self):
        assert self.pixels_page.event_set_value_field_is_displayed()

    def check_event_time_period_fields(self):
        assert self.pixels_page.event_time_period_field_is_displayed()
        assert self.pixels_page.event_amount_field_is_displayed()

    def check_event_js_field_displayed(self):
        assert self.pixels_page.event_js_field_is_displayed()

    def check_right_side_bar_opened(self):
        assert self.pixels_page.right_side_bar_opened()

    def check_sync_user_warning(self):
        assert self.pixels_page.sync_user_warning_displayed()

    def check_data_layer_fields(self):
        assert self.pixels_page.data_layer_field_displayed()
        assert self.pixels_page.data_layer_warning_displayed()

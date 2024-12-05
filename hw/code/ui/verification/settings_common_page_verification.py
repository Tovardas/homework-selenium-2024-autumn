class SettingsCommonPageVerification:
    def __init__(self, settings_common_page):
        self.settings_common_page = settings_common_page

    def check_page_elements_visibility(self):
        assert self.settings_common_page.inputs_became_visible()
        assert self.settings_common_page.buttons_became_visible()

    def check_phone_number_error(self):
        assert self.settings_common_page.get_phone_number_error() == self.settings_common_page.ERROR_INVALID_PHONE_NUMBER

    def check_additional_email_inputs_visibility(self):
        email_fields_counter = 0
        self.settings_common_page.click_add_email_button()
        assert self.settings_common_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        self.settings_common_page.click_add_email_button()
        assert self.settings_common_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        self.settings_common_page.click_add_email_button()
        assert self.settings_common_page.additional_email_input_became_visible(email_fields_counter)

    def check_email_error(self):
        assert self.settings_common_page.get_email_error() == self.settings_common_page.ERROR_INVALID_EMAIL

    def check_empty_field_errors(self):
        assert self.settings_common_page.get_email_error() == self.settings_common_page.ERROR_EMPTY_FIELD
        assert self.settings_common_page.get_full_name_error() == self.settings_common_page.ERROR_EMPTY_FIELD
        assert self.settings_common_page.get_inn_error() == self.settings_common_page.ERROR_EMPTY_FIELD

    def check_inn_error(self, error_type):
        if error_type == 'too_short':
            assert self.settings_common_page.get_inn_error() == self.settings_common_page.ERROR_TOO_SHORT_INN
        elif error_type == 'invalid':
            assert self.settings_common_page.get_inn_error() == self.settings_common_page.ERROR_INVALID_INN

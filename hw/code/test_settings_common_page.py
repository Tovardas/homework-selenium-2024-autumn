from base_case import BaseCase


class TestSettingsCommonPage(BaseCase):
    FULL_NAME = 'Tester T T'
    INN = '123456789012'

    def test_is_page_became_visible(self, settings_common_page):
        assert settings_common_page.inputs_became_visible()
        assert settings_common_page.buttons_became_visible()

    def test_is_error_invalid_phone_number(self, settings_common_page):
        settings_common_page.enter_phone_number('7985285313')
        assert settings_common_page.get_phone_number_error() == settings_common_page.ERROR_INVALID_PHONE_NUMBER

    def test_is_additional_email_inputs_became_visible(self, settings_common_page):
        email_fields_counter = 0
        settings_common_page.click_add_email_button()
        assert settings_common_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        settings_common_page.click_add_email_button()
        assert settings_common_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        settings_common_page.click_add_email_button()
        assert settings_common_page.additional_email_input_became_visible(email_fields_counter)

    def test_is_error_invalid_email(self, settings_common_page):
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('invalid')
        assert settings_common_page.get_email_error() == settings_common_page.ERROR_INVALID_EMAIL

    def test_is_error_empty_fields(self, settings_common_page):
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('')
        assert settings_common_page.get_email_error() == settings_common_page.ERROR_EMPTY_FIELD
        assert settings_common_page.get_full_name_error() == settings_common_page.ERROR_EMPTY_FIELD
        assert settings_common_page.get_inn_error() == settings_common_page.ERROR_EMPTY_FIELD

    def test_is_error_too_short_inn(self, settings_common_page):
        settings_common_page.enter_inn('123456')
        assert settings_common_page.get_inn_error() == settings_common_page.ERROR_TOO_SHORT_INN

    def test_is_error_invalid_inn(self, settings_common_page):
        settings_common_page.enter_inn('11111111111a')
        assert settings_common_page.get_inn_error() == settings_common_page.ERROR_INVALID_INN

    def test_logout_other_devices(self, settings_common_page):
        settings_common_page.click_logout_other_devices_button()
        assert settings_common_page.logout_devices_success_message_became_visible()

    def test_is_delete_cabinet_modal_page_became_visible(self, settings_common_page):
        settings_common_page.click_delete_cabinet_button()
        assert settings_common_page.delete_cabinet_modal_page_became_visible()

    def test_cancel_changes(self, settings_common_page):
        full_name_before = settings_common_page.get_full_name_field_value()
        settings_common_page.enter_full_name(self.FULL_NAME)
        settings_common_page.click_cancel_button()
        assert settings_common_page.get_full_name_field_value() == full_name_before

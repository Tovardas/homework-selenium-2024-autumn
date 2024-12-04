import time
from base_case import BaseCase


class TestSettingsNotificationsPage(BaseCase):
    def test_h2_became_visible(self, settings_notifications_page):
        assert settings_notifications_page.h2_became_visible()
        assert settings_notifications_page.checkbox_became_visible()
        assert settings_notifications_page.switch_email_became_visible()
        assert settings_notifications_page.telegram_became_visible()


    def test_is_on_cancel_click_checkbox_returned(self, settings_notifications_page):
        checked = settings_notifications_page.checkbox_checked()
        settings_notifications_page.click_checkbox()
        settings_notifications_page.click_cancel()

        if checked:
            assert settings_notifications_page.checkbox_checked()
        else:
            assert settings_notifications_page.checkbox_not_checked()

    def test_is_on_save_click_checkbox_saved(self, settings_notifications_page):
        checked = settings_notifications_page.checkbox_checked()
        settings_notifications_page.click_checkbox()
        settings_notifications_page.click_save()

        if checked:
            assert settings_notifications_page.checkbox_not_checked()
        else:
            assert settings_notifications_page.checkbox_checked()

class SettingsNotificationsPageVerification:
    def __init__(self, settings_notifications_page):
        self.settings_notifications_page = settings_notifications_page

    def check_elements_visibility(self):
        assert self.settings_notifications_page.h2_became_visible()
        assert self.settings_notifications_page.checkbox_became_visible()
        assert self.settings_notifications_page.switch_email_became_visible()
        assert self.settings_notifications_page.telegram_became_visible()

    def check_checkbox_state(self, expected_state):
        if expected_state:
            assert self.settings_notifications_page.checkbox_checked()
        else:
            assert self.settings_notifications_page.checkbox_not_checked()

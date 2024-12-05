class SettingsAccessPageVerification:
    def __init__(self, settings_access_page):
        self.settings_access_page = settings_access_page

    def check_header_and_sign_visibility(self):
        assert self.settings_access_page.header_and_sign_became_visible()
        assert self.settings_access_page.add_button_became_visible()

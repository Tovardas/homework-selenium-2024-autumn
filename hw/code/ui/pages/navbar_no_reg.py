from ui.locators.navbar_no_reg_locators import NavbarNoRegLocators
from ui.pages.base_page import BasePage


class NavbarNoReg(BasePage):
    locators = NavbarNoRegLocators()

    def click_news_button(self):
        self.click(self.locators.NAVBAR_NEWS_NAME)

    def click_cases_button(self):
        self.click(self.locators.NAVBAR_CASES_NAME)

    def click_forum_button(self):
        self.click(self.locators.NAVBAR_FORUM_NAME)

    def click_auth_button(self):
        self.click(self.locators.NAVBAR_AUTH_NAME)

    def click_logo_button(self):
        self.click(self.locators.NAVBAR_LOGO_ICON)

    def click_monetize_button(self):
        self.click(self.locators.NAVBAR_MONETIZE_NAME)

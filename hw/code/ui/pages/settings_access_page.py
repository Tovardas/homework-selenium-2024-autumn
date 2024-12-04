from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.settings_access_page_locators import SettingsAccessPageLocators


class SettingsAccessPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/access'
    locators = SettingsAccessPageLocators()

    def click_add_button(self):
        self.click(self.locators.ADD_BUTTON)

    def click_more_link(self):
        self.click(self.locators.ACCESS_EMPTY_MORE_LINK)

    def add_modal_became_visible(self):
        return self.became_visible(self.locators.MODAL)
    
    def add_button_became_visible(self):
        return self.became_visible(self.locators.ADD_BUTTON)
    
    def header_and_sign_became_visible(self):
        return self.became_visible(self.locators.ACCESS_EMPTY_HEADER) and self.became_visible(self.locators.ACCESS_EMPTY_SIGN) and self.became_visible(self.locators.ACCESS_EMPTY_MORE_LINK)
    
    def redirected(self):
        return self.is_opened('https://ads.vk.com/help/articles/additionalaccounts')
    
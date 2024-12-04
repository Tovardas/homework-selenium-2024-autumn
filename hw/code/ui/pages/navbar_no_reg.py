from ui.pages.base_page import BasePage
from selenium.webdriver import Keys
from ui.locators.navbar_no_reg_locators import NavbarNoRegLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time


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
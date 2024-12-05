import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.locators.auth_page_locators import AuthPageLocators
from ui.pages.base_page import BasePage


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.MAIL_RU_LOGIN)
        )

        login_input = self.find(self.locators.MAIL_RU_LOGIN)
        login_input.clear()
        login_input.send_keys(login)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.MAIL_RU_NEXT_BUTTON)
        )

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.AUTH_PROBLEMS_BUTTON)
        )

        self.click(self.locators.AUTH_PROBLEMS_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.USE_PASSWORD_BUTTON)
        )

        self.click(self.locators.USE_PASSWORD_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.MAIL_RU_PASSWORD)
        )

        password_input = self.find(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.MAIL_RU_SUBMIT_BUTTON)
        )

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)

        if self.became_visible(self.locators.CONFIRMATION):
            confirmation = self.find(self.locators.CONFIRMATION)
            confirmation.click()
            password_input = self.find(self.locators.MAIL_RU_PASSWORD)
            password_input.clear()
            password_input.send_keys(password)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.MAIL_RU_SUBMIT_BUTTON)
            )
            time.sleep(30)

        if self.became_visible(self.locators.CLOSE_GUIDE_BUTTON):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.CLOSE_GUIDE_BUTTON)
            )
            self.click(self.locators.CLOSE_GUIDE_BUTTON)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.OVERVIEW_BUTTON)
            )
        self.click(self.locators.OVERVIEW_BUTTON)

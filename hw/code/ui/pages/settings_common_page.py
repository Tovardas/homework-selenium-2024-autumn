from selenium.webdriver import Keys
from ui.locators.settings_common_page_locators import SettingsCommonPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsCommonPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = SettingsCommonPageLocators()

    ERROR_INVALID_PHONE_NUMBER = 'Некорректный номер телефона'
    ERROR_INVALID_EMAIL = 'Некорректный email адрес'
    ERROR_EMPTY_FIELD = 'Обязательное поле'
    ERROR_TOO_SHORT_INN = 'Длина ИНН должна быть 12 символов'
    ERROR_INVALID_INN = 'Некорректный ИНН'

    def inputs_became_visible(self):
        return self.became_visible(self.locators.PHONE_NUMBER_INPUT) and self.became_visible(
            self.locators.FULL_NAME_INPUT) and self.became_visible(self.locators.INN_INPUT)

    def buttons_became_visible(self):
        return self.became_visible(self.locators.ADD_EMAIL_BUTTON) and self.became_visible(
            self.locators.DELETE_CABINET_BUTTON) and self.became_visible(self.locators.LOGOUT_OTHER_DEVICES_BUTTON)

    def enter_full_name(self, full_name: str):
        full_name_input = self.find(self.locators.FULL_NAME_INPUT)
        full_name_input.clear()
        full_name_input.send_keys(full_name)
        full_name_input.send_keys(Keys.ENTER)

    def get_full_name_field_value(self) -> str:
        return self.find(self.locators.FULL_NAME_INPUT).get_attribute('value')

    def get_inn_field_value(self) -> str:
        return self.find(self.locators.INN_INPUT).get_attribute('value')

    def get_email_field_value(self):
        return self.find(self.locators.ADDITIONAL_EMAIL_INPUT(0)).get_attribute('value')

    def get_phone_number_value(self):
        return self.find(self.locators.PHONE_NUMBER_INPUT).get_attribute('value')


    def is_full_name_matches(self, full_name: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.get_full_name_field_value() == full_name
            )
            return True
        except TimeoutException:
            return False

    def is_inn_matches(self, inn: str, timeout: int = 5)-> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.get_inn_field_value() == inn
            )
            return True
        except TimeoutException:
            return False

    def is_phone_matches(self, phone: str, timeout: int = 5)-> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.get_phone_number_value() == phone
            )
            return True
        except TimeoutException:
            return False


    def is_email_matches(self, email: str, timeout: int = 5)-> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.get_email_field_value() == email
            )
            return True
        except TimeoutException:
            return False

    def save_and_cancel_buttons_became_visible(self) -> bool:
        return (self.became_visible(self.locators.SAVE_BUTTON)
                and self.became_visible(self.locators.CANCEL_BUTTON))

    def enter_phone_number(self, phone_number: str):
        phone_number_input = self.find(self.locators.PHONE_NUMBER_INPUT)
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)
        phone_number_input.send_keys(Keys.ENTER)

    def get_phone_number_error(self) -> str:
        return self.find(self.locators.PHONE_NUMBER_ERROR).text

    def click_add_email_button(self):
        self.click(self.locators.ADD_EMAIL_BUTTON)

    def additional_email_input_became_visible(self, counter: int) -> bool:
        return self.became_visible(self.locators.ADDITIONAL_EMAIL_INPUT(counter))

    def enter_email(self, email: str, counter: int = 0):
        email_input = self.find(self.locators.ADDITIONAL_EMAIL_INPUT(counter))
        email_input.clear()
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)



    def get_email_error(self) -> str:
        return self.find(self.locators.EMAIL_ERROR).text

    def get_full_name_error(self) -> str:
        return self.find(self.locators.FULL_NAME_ERROR).text

    def enter_inn(self, inn: str):
        inn_input = self.find(self.locators.INN_INPUT)
        inn_input.clear()
        inn_input.send_keys(inn)
        inn_input.send_keys(Keys.ENTER)

    def get_inn_error(self) -> str:
        return self.find(self.locators.INN_ERROR).text

    def click_logout_other_devices_button(self):
        self.click(self.locators.LOGOUT_OTHER_DEVICES_BUTTON)

    def logout_devices_success_message_became_visible(self) -> bool:
        return self.became_visible(self.locators.LOGOUT_OTHER_DEVICES_SUCCESS_MESSAGE)

    def click_delete_cabinet_button(self):
        self.click(self.locators.DELETE_CABINET_BUTTON)

    def delete_cabinet_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.DELETE_CABINET_MODAL_PAGE)

    def click_save_button(self):
        self.click(self.locators.SAVE_BUTTON)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

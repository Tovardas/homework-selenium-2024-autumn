from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class SettingsNotificationsPageLocators(BasePageLocators):

    @staticmethod
    def H2_NAME(h2):
        return (By.XPATH, f"//*[contains(@class, 'vkuiTitle--level-2') and text()='{h2}']")
    
    @staticmethod
    def CHECKBOX_NAME(checkbox):
        return (By.XPATH, f"//*[contains(@class, 'Subscriptions_checkboxContent__') and text()='{checkbox}']")
    
    @staticmethod
    def CHECKBOX_NAME_IS_CHECKED_OR_NOT(checkbox, state):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCheckbox') and .//* [contains(@class, 'Subscriptions_checkboxContent__') and text()='{checkbox}']]//*[contains(@class, 'vkuiCheckbox__icon--{state}')]")

    SWITCH_EMAIL_SIGN = (By.XPATH, "//*[contains(@class, 'Emails_item__')]")
    SWITCH_EMAIL_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiSimpleCell')]//label[contains(@class, 'vkuiSwitch')]")

    TELEGRAM_SIGN = (By.XPATH, "//*[contains(@class, 'Telegram_title__') and text()='Сообщение в Telegram']")
    TELEGRAM_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Подключить']")

    SAVE_MODAL = (By.XPATH, "//*[contains(@class, 'Notifications_bottom__')]")

    SAVE_MODAL_CANCEL = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Отменить']")
    SAVE_MODAL_SAVE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Сохранить']")
from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class SettingsAccessPageLocators(BasePageLocators):
    ACCESS_EMPTY_HEADER = (
    By.XPATH, "//*[contains(@class, 'vkuiPlaceholder__header') and text()='Доступа к другим кабинетам пока нет']")
    ACCESS_EMPTY_SIGN = (By.XPATH, "//*[contains(@class, 'vkuiText')]")

    ACCESS_EMPTY_MORE_LINK = (By.XPATH, "//*[contains(@class, 'vkuiLink') and text()='Подробнее']")

    ADD_BUTTON = (By.XPATH, "//*[@data-testid='add-user']")

    MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]")

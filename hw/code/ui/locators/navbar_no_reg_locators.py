from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class NavbarNoRegLocators(BasePageLocators):
    NAVBAR_NEWS_NAME = (
    By.XPATH, "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Новости')]]")
    NAVBAR_CASES_NAME = (
    By.XPATH, "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Кейсы')]]")
    NAVBAR_FORUM_NAME = (
    By.XPATH, "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Форум идей')]]")
    NAVBAR_AUTH_NAME = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary__LCfol')]")
    NAVBAR_LOGO_ICON = (By.XPATH, "//div[contains(@class, 'content_logo__GA44t')]")
    NAVBAR_MONETIZE_NAME = (
    By.XPATH, "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Монетизация')]]")

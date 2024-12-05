from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    MAIL_RU_LOGIN = (By.NAME, 'username')
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    MAIL_RU_SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")
    AUTH_PROBLEMS_BUTTON = (By.XPATH, "//*[@data-test-id='auth-problems']")
    USE_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Использовать пароль для входа')]")
    CLOSE_GUIDE_BUTTON = (By.XPATH,
                          "//div[@tabindex='0' and @role='button' and @aria-label='Закрыть' and @class='vkuiModalDismissButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']")
    OVERVIEW_BUTTON = (By.XPATH, "//a[@href='/hq/overview']")
    CONFIRMATION = (By.XPATH, "//button[span[contains(text(),'Это я')]]")

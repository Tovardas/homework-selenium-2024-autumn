from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class CenterCommercePageLocators(BasePageLocators):
    CREATE_CATALOG_BUTTON = (
        By.XPATH, 
        "//*[contains(@class, 'vkuiButton__content') and text()='Создать каталог']"
    )
    TRAINING_BUTTON = (
        By.XPATH, 
        "//button[@data-testid='ecomm-onboarding-start']"
    )
    CATALOG_MODAL_PAGE = (
        By.CLASS_NAME, 
        "ModalSidebarPage_container__Zopae"
    )
    
    CATALOG_CLOSE_BUTTON = (
        By.XPATH, 
        "//button[@type='button' and @aria-label='Close']"
    )
    CATALOG_CANCEL_BUTTON = (
        By.XPATH, 
        "//button[@data-testid='cancel' and .//span[contains(@class, 'vkuiButton__content') and text()='Отмена']]"
    )

    LEARNING_MODAL = (By.CLASS_NAME, "vkuiModalCardBase__container")
    LEARNING_MODAL_DISMISS_BUTTON = (
        By.XPATH, 
        "//button[@class='vkuiButton vkuiButton--size-l vkuiButton--mode-secondary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--sizeY-none vkuiButton--stretched vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']//*[contains(text(),'Не сейчас')]"
    )
    LEARNING_MODAL_CLOSE_BUTTON = (
        By.XPATH, 
        "//div[@class='vkuiModalDismissButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']//*[name()='svg']"
    )

    CHOICE_LEARNING_MODAL = (By.CLASS_NAME, "vkuiModalPage__content-wrap")
    CHOICE_LEARNING_MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR, 
        "div.vkuiModalDismissButton[aria-label='Закрыть']"
    )

    CATALOG_NAME_INPUT = (
        By.CSS_SELECTOR, 
        'input[data-testid="catalogName-input"]'
    )
    REQUIRED_FIELD_ERROR = (
        By.CSS_SELECTOR, 
        'span.vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote[role="alert"]'
    )
    CATALOG_SOURCE_TYPE_FEED = (By.XPATH, "//div[@data-entityid='url']")
    CATALOG_SOURCE_TYPE_MARKETPLACE = (By.XPATH, "//div[@data-entityid='marketplace']")
    CATALOG_SOURCE_TYPE_FILE = (By.XPATH, "//div[@data-entityid='file']")

    FEED_URL_INPUT = (By.CSS_SELECTOR, 'input[data-testid="catalogUrl-input"]')
    REFRESH_PERIOD_SELECT = (By.CSS_SELECTOR, 'input[data-testid="catalogPeriod-select"]')
    UTM_CHECKBOX = (
        By.XPATH, 
        "//span[text()='Автоматически удалять UTM-метки']"
    )

    MARKETPLACE_URL_INPUT = (By.CSS_SELECTOR, 'input[data-testid="catalogUrl-input"]')
    API_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите ключ API"]')

    FEED_CATEGORY_SELECT = (By.XPATH, "//span[text()='Категория фида']")
    FEED_FILE_INPUT = (By.XPATH, "//span[text()='Файл фида']")

    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")

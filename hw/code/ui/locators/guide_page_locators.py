from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class GuidePageLocators(BasePageLocators):
    GUIDE_BUTTON = (
        By.XPATH, 
        "//*[text()='Обучение']"
    )
    GUIDE_CLOSE_BUTTON = (
        By.CLASS_NAME,
        "vkuiModalDismissButton"
    )
    GUIDE_MODAL = (
        By.CLASS_NAME, 
        "ModalRoot_componentWrapper__uzHTL"
    )

    INNER_MODAL = (
        By.CLASS_NAME, 
        "SelectOnboardingModal_root__wPDGY"
    )
    COMMUNITY_BUTTON = (
        By.XPATH, 
        "//*[text()='Сообщество ВКонтакте']"
    )

    CAMPAIGN_MODAL_BUTTON = (
        By.XPATH, 
        "//*[text()='Настроить кампанию с подсказками']"
    )
    CAMPAIGN_BUTTON = (
        By.XPATH, 
        "//*[text()='Создать кампанию']"
    )
   
    VIDEO_MODAL = (
        By.CLASS_NAME, 
        "VideoOnboardingModal_modal__EMA4v"
    )
    VIDEO_BUTTON = (
        By.XPATH, 
        "//*[text()='Смотреть видеоурок от экспертов VK']"
    )

    CATALOG_BUTTON = (
        By.XPATH, 
        "//*[text()='Каталог товаров']"
    )

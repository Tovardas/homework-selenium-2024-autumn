from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class GuidePageLocators(BasePageLocators):
    GUIDE_BUTTON = (
        By.XPATH,
        "(//*[text()='Пройти обучение'])"
    )

    HELP_AND_GUIDE = (By.XPATH, "//div[@data-testid='help-menu-container']//div[@role='button' and @data-route='help']")

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

    PIXEL_BUTTON = (
        By.XPATH,
        "//*[text()='Сайт']"
    )

    CATALOG_BUTTON = (
        By.XPATH,
        "//*[text()='Каталог товаров']"
    )

    MOBILE_BUTTON = (
        By.XPATH,
        "//*[text()='Мобильное приложение']"
    )

    LIDFORMS_BUTTON = (
        By.XPATH,
        "//*[text()='Лид-формы']"
    )

    MINIAPPS_BUTTON = (
        By.XPATH,
        "//*[text()='VK Mini Apps']"
    )

    MUSIC_BUTTON = (
        By.XPATH,
        "//*[text()='Музыка']"
    )

    VIDEO_BUTTON = (
        By.XPATH,
        "//*[text()='Видео и трансляции']"
    )

    DZEN_BUTTON = (
        By.XPATH,
        "//*[text()='Дзен']"
    )

    CAMPAIGN_MODAL_BUTTON = (
        By.XPATH,
        "//*[text()='Настроить кампанию с подсказками']"
    )

    CAMPAIGN_BUTTON = (
        By.XPATH,
        "//*[text()='Создать кампанию']"
    )

    PIXEL_VIDEO_BUTTON = (
        By.XPATH,
        "//*[text()='Смотреть видеоурок от экспертов VK']"
    )

    PIXEL_PLATFORM_BUTTON = (
        By.XPATH,
        "//*[text()='Смотреть курс на обучающей платформе']"
    )

    PIXEL_VIDEO_ELEMENT = (
        By.XPATH,
        "//div[@id='video_player']"
    )

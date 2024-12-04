from operator import contains

from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class GuideNoRegPageLocators(BasePageLocators):
    GUIDE_NAME = (By.XPATH,  "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Обучение')]]")
    GUIDE_MATERIALS_NAME = (By.XPATH,  "//div[contains(@class, 'list_item__UURnC') and .//text()[contains(., 'Полезные материалы')]]")
    GUIDE_EVENTS_NAME = (By.XPATH, "//div[contains(@class, 'list_item__UURnC') and .//text()[contains(., 'Мероприятия')]]")
    GUIDE_VIDEOS_NAME = (By.XPATH, "//div[contains(@class, 'list_item__UURnC') and .//text()[contains(., 'Видеокурсы')]]")
    GUIDE_CERTIFICATION_NAME = (By.XPATH, "//div[contains(@class, 'list_item__UURnC') and .//text()[contains(., 'Сертификация')]]")

    MATERIALS_CARD = (By.XPATH, "//button[contains(@class, 'insight-card_button__qCQCn')]")
    MATERIALS_TAG = (By.XPATH, "//a[contains(@class, 'Tags_item__qi6Xa') and .//text()[contains(., 'Маркетинг')]]")
    MATERIALS_CONTENT_LINK = (By.XPATH, "//button[contains(@class, 'vkuiLink') and .//text()[contains(., 'Слишком быстрый расход')]]")
    MATERIALS_CONTENT_HEADER = (By.XPATH, "//h2[contains(text(), 'Слишком быстрый расход')]")
    MATERIALS_CABINET_NAME = (By.XPATH, "//a[contains(@class, 'vkuiButton') and .//text()[contains(., 'В кабинет')]]")
    MATERIALS_PAGINATION_NUMBER = (By.XPATH, "//div[contains(@class, 'vkuiPagination__page') and .//text()[contains(., '3')]]")
    MATERIALS_PAGINATION_LEFT = (By.XPATH, "//li[contains(@class, 'vkuiPagination__prevButtonContainer')]")
    MATERIALS_PAGINATION_RIGHT = (By.XPATH, "//li[contains(@class, 'vkuiPagination__nextButtonContainer')]")

    EVENTS_CARD_OLD = (By.XPATH, "//a[contains(@class, 'event-card_wrapper__GZkvu') and .//text()[contains(., 'Как подготовить материалы для быстрой модерации на платформах VK')]]")
    EVENTS_CARD_NEW =(By.XPATH, "//a[contains(@class, 'event-card_wrapper__GZkvu') and .//text()[contains(., 'Как продвигать бизнес в новогодние праздники')]]")
    EVENTS_VIDEO = (By.XPATH, "//div[@id='video_player']")
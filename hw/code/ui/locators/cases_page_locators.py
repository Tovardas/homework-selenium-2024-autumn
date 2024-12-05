from operator import contains

from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class CasesPageLocators(BasePageLocators):
    CASES_BUTTON = (By.XPATH,  "//div[contains(@class, 'navigation_item__zSI_a') and .//text()[contains(., 'Кейсы')]]")
    CASES_CARD = (By.XPATH, "//a[@class='case-card_wrapper__N1Mya' and @href='/cases/snizhaem-cpf-v-4-raza-kejs-burger-king']")
    CASES_TAG = (By.XPATH, "//a[contains(@class, 'Tags_item__qi6Xa') and .//text()[contains(., 'Ретаргетинг')]]")
    CASES_CONTENT_LINK = (By.XPATH, "//button[contains(@class, 'vkuiLink') and .//text()[contains(., 'Результаты')]]")
    CASES_CONTENT_HEADER = (By.XPATH, "//h2[contains(text(), 'Результаты')]")
    CASES_CABINET_NAME = (By.XPATH, "//a[contains(@class, 'vkuiButton') and .//text()[contains(., 'В кабинет')]]")
    CASES_PAGINATION_NUMBER = (By.XPATH, "//div[contains(@class, 'vkuiPagination__page') and .//text()[contains(., '3')]]")
    CASES_PAGINATION_LEFT = (By.XPATH, "//li[contains(@class, 'vkuiPagination__prevButtonContainer')]")
    CASES_PAGINATION_RIGHT = (By.XPATH, "//li[contains(@class, 'vkuiPagination__nextButtonContainer')]")
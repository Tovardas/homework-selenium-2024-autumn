from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.locators.audience_page_locators import AudiencePageLocators
from ui.pages.base_page import BasePage


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    SOURCE_TYPE_LIST = ['Существующая аудитория', 'Список пользователей', 'Ключевые фразы',
                        'События в рекламной кампании', 'События в мобильном приложении', 'События в лид-форме',
                        'События на сайте', 'Подписчики сообществ', 'Музыканты',
                        'Пользователи VK Mini Apps и игр ВКонтакте']
    ERROR_TOO_LONG_AUDIENCE_NAME = 'Напишите текст не больше 255 символов'

    def cross_button_became_visible(self):
        return self.became_visible(self.locators.CROSS_BUTTON)

    def create_audience_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CREATE_AUDIENCE_MODAL_PAGE, timeout=1)

    def create_audience_modal_page_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.CREATE_AUDIENCE_MODAL_PAGE, timeout=1)

    def audience_name_input_became_visible(self):
        return self.became_visible(self.locators.AUDIENCE_NAME_INPUT)

    def add_source_button_became_visible(self):
        return self.became_visible(self.locators.ADD_SOURCE_BUTTON)

    def footer_buttons_became_visible(self):
        return self.became_visible(self.locators.CANCEL_BUTTON) and self.became_visible(self.locators.SUBMIT_BUTTON)

    def click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON, timeout=1)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON, timeout=1)

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON)

    def add_source_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.ADD_SOURCE_MODAL_PAGE)

    def add_source_modal_page_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.ADD_SOURCE_MODAL_PAGE)

    def source_items_became_visible(self):
        for s in self.SOURCE_TYPE_LIST:
            if not self.became_visible(self.locators.SOURCE_ITEM(s)):
                return False
        return True

    def key_phrases_sidebar_became_visible(self):
        return self.became_visible(self.locators.KEY_PHRASES_MODAL_PAGE)

    def key_phrases_textarea_became_visible(self):
        return self.became_visible(self.locators.KEY_PHRASES_INPUT)

    def minus_key_phrases_textarea_became_visible(self):
        return self.became_visible(self.locators.MINUS_PHRASES_INPUT)

    def sidebar_sign_became_visible(self):
        return self.became_visible(self.locators.SIDEBAR_SIGN) and self.became_visible(self.locators.SIDEBAR_SIGN_HINTS)

    def period_input_became_visible(self):
        return self.became_visible(self.locators.PERIOD_INPUT)

    def select_source(self, source_name):
        self.click(self.locators.SOURCE_ITEM(source_name))

    def enter_key_phrases(self, key_phrases: list):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(key_phrases))

    def enter_minus_phrases(self, key_phrases: list):
        key_phrases_input = self.find(self.locators.MINUS_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(key_phrases))

    def enter_groups(self, groups: list):
        key_phrases_input = self.find(self.locators.GROUPS)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(groups))

    def edit_audience(self, name: str):
        self.click(self.locators.OPTIONS)
        self.scroll_and_click(self.locators.NEW_OPTIONS(name))

    def click_modal_page_submit_button(self):
        self.became_visible(self.locators.AUDIENCE_READY)
        try:
            self.click(self.locators.MODAL_PAGE_SUBMIT_BUTTON, timeout=5)
        except TimeoutException:
            pass

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE, timeout=10).text

    def delete_audience(self):
        self.click(self.locators.DELETE)
        self.click(self.locators.DELETE_MODAL_BUTTON)

    def created_audience_became_invisible(self):
        return self.became_invisible(self.locators.CREATED_AUDIENCE_TITLE)

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def audience_modal_became_visible(self) -> bool:
        return self.became_visible(self.locators.AUDIENCE_CREATE_MODAL)

    def click_audience_add_source_button(self):
        self.click(self.locators.AUDIENCE_ADD_SOURCE_BUTTON)

    def audience_add_source_modal_became_visible(self) -> bool:
        return self.became_visible(self.locators.AUDIENCE_SOURCE_MODAL)

    def click_audience_source_phrase_button(self):
        self.click(self.locators.AUDIENCE_SOURCE_PHRASE_BUTTON)

    def enter_source_name(self, str):
        musician_input = self.find(self.locators.AUDIENCE_SOURCE_NAME_INPUT)
        musician_input.send_keys(str)

    def enter_phrase_name(self, str):
        musician_input = self.find(self.locators.AUDIENCE_SOURCE_PHRASE_INPUT)
        musician_input.send_keys(str)

    def click_save_phrase_button(self):
        self.click(self.locators.SAVE_PHRASE_BUTTON)

    def click_save_button0(self):
        self.click(self.locators.SAVE_BUTTON_0)

    def click_save_button1(self):
        self.click(self.locators.SAVE_BUTTON_1)

    def click_save_button2(self):
        self.click(self.locators.SAVE_BUTTON_2)

    def click_save_button3(self):
        self.click(self.locators.SAVE_BUTTON_3)

    def audience_item_became_visible(self) -> bool:
        return self.became_visible(self.locators.AUDIENCE_ITEM)

    def click_cancel_source_button(self):
        self.click(self.locators.CANCEL_SOURCE_BUTTON, timeout=1)

    def hover_and_click_delete(self):
        audience_menu = self.find(self.locators.AUDIENCE_MENU)
        ActionChains(self.driver).move_to_element(audience_menu).perform()
        audience_menu.click()
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.DELETE_BUTTON)
        )
        delete_button.click()

    def audience_item_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.AUDIENCE_ITEM)

    def click_delete_confirm_button(self):
        self.click(self.locators.DELETE_CONFIRM_BUTTON, timeout=2)

    def delete_confirm_modal_became_visible(self) -> bool:
        return self.became_visible(self.locators.DELETE_CONFIRM_MODAL)

    def seach_audience_by_name(self, audience_name: str):
        elem = self.find(self.locators.SEARCH_INPUT)
        self.driver.execute_script("arguments[0].value = '';", elem)
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

from time import sleep

from ui.pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ui.locators.pixels_page_locators import PixelsPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PixelsPage(BasePage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = PixelsPageLocators()

    USER_CONVERSIONS = 'Пользовательские конверсии'
    EVENT_HREF = 'Посещена страница'
    TIME_PERIOD = 'Просмотрено страниц'
    TIME_PERIOD_FIELD = 'За посещение'
    EVENT_JS = 'Произошло JS-событие'


    def is_element_displayed(self, locator):
        try:
            self.wait().until(EC.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False


    def click_pixel_button(self):
        self.click(self.locators.CREATE_PIXEL_BUTTON)

    def pixel_modal_became_visible(self) -> bool:
        return self.became_visible(self.locators.PIXEL_MODAL_WINDOW)

    def enter_pixel_domain(self, url):
        site_field = self.find(self.locators.PIXEL_DOMAIN_FIELD)
        site_field.clear()
        site_field.send_keys(url)

    def enter_pixel_id_info(self, id, email):
        site_id_field = self.find(self.locators.MODAL_ID_PIXEL_FIELD)
        site_id_field.clear()
        site_id_field.send_keys(id)

        site_email_field = self.find(self.locators.MODAL_EMAIL_PIXEL_FIELD)
        site_email_field.clear()
        site_email_field.send_keys(email)

    def click_add_pixel_button(self):
        self.click(self.locators.PIXEL_ADD_BUTTON)

    def click_pixel_main_button(self):
        self.click(self.locators.PIXEL_MAIN_BUTTON)


    def click_id_pixel_modal_button(self):
        self.click(self.locators.PIXEL_ID_MODAL_BUTTON)

    def pixel_domain_error_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.INCORRECT_PIXEL_ERROR)

    def pixel_id_error_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.INCORRECT_PIXEL_ID_ERROR)

    def pixel_email_error_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.INCORRECT_PIXEL_EMAIL_ERROR)

    def pixel_email_required_error_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.INCORRECT_PIXEL_EMAIL_REQUIRED_ERROR)

    def click_create_new_pixel_conf(self):
        self.click(self.locators.MODAL_CREATE_NEW_PIXEL_CONF)

    def pixel_creation_success(self) -> bool:
        return self.is_element_displayed(self.locators.MODAL_CREATION_SUCCESS)

    def close_pixel_creation_success(self):
        self.click(self.locators.MODAL_CREATION_SUCCESS_CANCEL)

    def delete_pixel_true(self):
        self.hover(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.PIXEL_DELETE_BUTTON)
        self.click(self.locators.PIXEL_DELETE_CONF)

    def delete_pixel_false(self):
        self.hover(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.PIXEL_DELETE_BUTTON)
        self.click(self.locators.PIXEL_DELETE_CONF_CANCEL)

    def rename_pixel_false(self):
        self.hover(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.PIXEL_RENAME_BUTTON)
        self.click(self.locators.PIXEL_RENAME_CONF_CANCEL)

    def rename_pixel_true(self, name):
        self.hover(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.FIRST_ADDED_PIXEL_MORE)
        self.click(self.locators.PIXEL_RENAME_BUTTON)
        site_rename_field = self.find(self.locators.MODAL_RENAME_PIXEL_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(name)
        self.click(self.locators.PIXEL_RENAME_CONF)


    def click_options(self):
        self.click(self.locators.OPTIONS_BUTTON)

    def click_options_code_pixel(self):
        self.click(self.locators.OPTIONS_CODE_PIXEL)

    def click_options_tags(self):
        self.click(self.locators.OPTIONS_TAGS)

    def switch_auto_search(self):
        self.click(self.locators.SWITCH_AUTO_SEARCH)

    def switch_data_layer(self):
        self.click(self.locators.SWITCH_DATA_LAYER)

    def switch_sync_user(self):
        self.click(self.locators.SWITCH_SYNC_USER)

    def data_layer_field_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.DATA_LAYER_FIELD)

    def data_layer_warning_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.DATA_LAYER_WARNING)

    def sync_user_warning_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.USER_SYNC_WARNING)

    def click_create_tag_button(self):
        self.click(self.locators.CREATE_TAG_BUTTON)

    def tag_name_field_error(self) -> bool:
        return self.is_element_displayed(self.locators.TAG_NAME_FIELD_ERROR)

    def click_new_tag_conf_false(self):
        self.click(self.locators.CREATE_TAG_CONF_FALSE)

    def click_new_tag_conf_true(self):
        self.click(self.locators.CREATE_TAG_CONF_TRUE)

    def enter_tag_name(self, name):
        site_field = self.find(self.locators.TAG_NAME_FIELD)
        site_field.clear()
        site_field.send_keys(name)

    def new_tag_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.TAG_NAME_ELEMENT)


    def click_new_event_button(self):
        self.click(self.locators.NEW_EVENT_BUTTON)

    def right_side_bar_opened(self) -> bool:
        return self.is_element_displayed(self.locators.RIGHT_SIDE_BAR)

    def click_new_event_conf_false(self):
        self.click(self.locators.NEW_EVENT_CONF_FALSE)

    def click_new_event_conf_true(self):
        self.click(self.locators.NEW_EVENT_CONF_TRUE)

    def enter_event_name(self, name):
        site_rename_field = self.find(self.locators.EVENT_NAME_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(name)

    def choose_event_category(self):
        self.scroll_and_click(self.locators.CATEGORY_SELECT_INPUT('Выберите категорию'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.USER_CONVERSIONS))


    def choose_event_requirement_href(self):
        self.scroll_and_click(self.locators.CATEGORY_SELECT_INPUT('Выберите условие'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.EVENT_HREF))

    def choose_event_requirement_js(self):
        self.scroll_and_click(self.locators.CATEGORY_SELECT_INPUT('Выберите условие'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.EVENT_JS))

    def choose_event_requirement_with_time_period(self):
        self.scroll_and_click(self.locators.CATEGORY_SELECT_INPUT('Выберите условие'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.TIME_PERIOD))

    def event_url_field_is_displayed(self):
        return self.is_element_displayed(self.locators.EVENT_URL_FIELD)

    def event_time_period_field_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.EVENT_TIME_PERIOD_FIELD)

    def event_amount_field_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.EVENT_AMOUNT_FIELD)

    def event_js_field_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.EVENT_JS_FIELD)

    def enter_event_time_period(self):
        self.scroll_and_click(self.locators.CATEGORY_SELECT_INPUT('За День'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.TIME_PERIOD_FIELD))

    def enter_event_amount(self, number):
        site_rename_field = self.find(self.locators.EVENT_AMOUNT_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(number)

    def enter_event_url_field(self, url):
        site_rename_field = self.find(self.locators.EVENT_URL_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(url)

    def enter_event_js_field(self, name):
        site_rename_field = self.find(self.locators.EVENT_JS_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(name)

    def click_event_set_value(self):
        self.click(self.locators.EVENT_SET_VALUE_BUTTON)

    def event_set_value_field_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.EVENT_VALUE_FIELD)

    def enter_event_set_value_field(self, number):
        site_rename_field = self.find(self.locators.EVENT_VALUE_FIELD)
        site_rename_field.clear()
        site_rename_field.send_keys(number)
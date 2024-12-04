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
        #clear не очищает поле....
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
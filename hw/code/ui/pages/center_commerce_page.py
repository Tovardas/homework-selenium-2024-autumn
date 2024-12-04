from ui.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from ui.locators.center_commerce_page_locators import CenterCommercePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class CenterCommercePage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CenterCommercePageLocators()

    def catalog_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CATALOG_MODAL_PAGE)

    def learning_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.LEARNING_MODAL)
    
    def choice_learning_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CHOICE_LEARNING_MODAL)
    
    def close_choice_learning_modal_page(self) -> bool:
        return self.click(self.locators.CHOICE_LEARNING_MODAL_CLOSE_BUTTON)

    def close_training_modal(self):
        self.click(self.locators.LEARNING_MODAL_DISMISS_BUTTON)

    def click_create_catalog_button(self):
        self.click(self.locators.CREATE_CATALOG_BUTTON)

    def click_training_button(self):
        self.click(self.locators.TRAINING_BUTTON)

    def сlick_choice_learning(self):
        self.click(self.locators.TRAINING_BUTTON)

    def cancel_catalog_button(self):
        self.click(self.locators.CATALOG_CANCEL_BUTTON)

    def close_catalog_button(self):
        self.click(self.locators.CATALOG_CLOSE_BUTTON)

    def is_element_displayed(self, locator):
        try:
            self.wait().until(EC.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False

    def input_empty_catalog_name(self):
        input_field = self.find(self.locators.CATALOG_NAME_INPUT)

        current_value = input_field.get_attribute('value')

        for _ in range(len(current_value)):
            input_field.send_keys(Keys.BACKSPACE)

    def input_invalid_feed_url(self):
        input_field = self.find(self.locators.FEED_URL_INPUT)

        input_field.clear()
        input_field.send_keys("мяу")

    def input_invalid_marketplace_url(self):
        input_field = self.find(self.locators.MARKETPLACE_URL_INPUT)

        input_field.clear()
        input_field.send_keys("чипи-чипи чапа-чапа")

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def is_required_field_error_displayed(self):
        return self.is_element_displayed(self.locators.REQUIRED_FIELD_ERROR)

    def select_feed_or_community(self):
        self.click(self.locators.CATALOG_SOURCE_TYPE_FEED)

    def field_feed_displayed(self):
        return self.is_element_displayed(self.locators.FEED_URL_INPUT)

    def field_period_displayed(self):
        return self.is_element_displayed(self.locators.REFRESH_PERIOD_SELECT)
    
    def field_utm_displayed(self):
        return self.is_element_displayed(self.locators.UTM_CHECKBOX)

    def select_marketplace(self):
        self.click(self.locators.CATALOG_SOURCE_TYPE_MARKETPLACE)

    def verify_marketplace_fields_visible(self):
        return self.is_element_displayed(self.locators.MARKETPLACE_URL_INPUT)

    def select_manually(self):
        self.click(self.locators.CATALOG_SOURCE_TYPE_FILE)

    def field_category_visible(self):
        return self.is_element_displayed(self.locators.FEED_CATEGORY_SELECT)

    def field_category_displayed(self):
        return self.is_element_displayed(self.locators.FEED_CATEGORY_SELECT)

    def field_feed_file_displayed(self):
        return self.is_element_displayed(self.locators.FEED_FILE_INPUT)
        
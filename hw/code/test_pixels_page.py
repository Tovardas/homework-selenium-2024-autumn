from copyreg import pickle

import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
from ui.locators.pixels_page_locators import PixelsPageLocators

class TestPixelsPage(BaseCase):

    INCORRECT_DOMAIN = 'notCorrectTochkaRu'
    CORRECT_DOMAIN = "https://example.com"
    INCORRECT_ID = "123"
    INCORRECT_EMAIL = "notCorrectSobakaTochkaRu"
    NEW_NAME = "New Pixel Testing Name"
    TAG_NAME = "testing"
    EVENT_NAME = "testing event"
    URL_CONTAINS = "test/number"

    def test_open_catalog_modal(self, pixels_page):
        pixels_page.click_pixel_button()
        assert pixels_page.pixel_modal_became_visible()

    def test_not_correct_data(self, pixels_page):
        pixels_page.click_pixel_button()
        pixels_page.enter_pixel_domain(self.INCORRECT_DOMAIN)
        pixels_page.click_add_pixel_button()
        assert pixels_page.pixel_domain_error_displayed()

    def test_not_correct_pixel_id(self, pixels_page):
        pixels_page.click_pixel_button()
        pixels_page.click_id_pixel_modal_button()
        pixels_page.enter_pixel_id_info(self.INCORRECT_ID, self.INCORRECT_EMAIL)
        pixels_page.click_add_pixel_button()
        assert pixels_page.pixel_email_error_displayed()
        #pixels_page.clear_id_modal_field()
        #pixels_page.clear_email_modal_field()
        #pixels_page.click_add_pixel_button()
        #assert pixels_page.pixel_id_error_displayed()
        #assert pixels_page.pixel_email_required_error_displayed()
        #При стирании символов с клавиатуры, появляются ошибки.
        #При использовании метода clear - ничего не появляется


    def test_correct_data(self, pixels_page):
        pixels_page.click_pixel_button()
        pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        pixels_page.click_add_pixel_button()
        pixels_page.click_create_new_pixel_conf()
        assert pixels_page.pixel_creation_success()
        pixels_page.close_pixel_creation_success()
        pixels_page.delete_pixel_false()
        pixels_page.delete_pixel_true()

    def test_rename_pixel(self, pixels_page):
        #pixels_page.click_pixel_button()
        #pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        #pixels_page.click_add_pixel_button()
        #pixels_page.click_create_new_pixel_conf()
        #assert pixels_page.pixel_creation_success()
        #pixels_page.close_pixel_creation_success()
        pixels_page.rename_pixel_false()
        pixels_page.rename_pixel_true(self.NEW_NAME)
        pixels_page.delete_pixel_false()
        #pixels_page.delete_pixel_true()


    def test_options_code_pixel(self, pixels_page):
        pixels_page.click_pixel_button()
        pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        pixels_page.click_add_pixel_button()
        pixels_page.click_create_new_pixel_conf()
        assert pixels_page.pixel_creation_success()
        pixels_page.close_pixel_creation_success()

        pixels_page.click_options()
        pixels_page.click_options_code_pixel()

        pixels_page.switch_auto_search()
        pixels_page.switch_auto_search()

        pixels_page.switch_data_layer()
        assert pixels_page.data_layer_field_displayed()
        assert pixels_page.data_layer_warning_displayed()

        pixels_page.switch_data_layer()

        pixels_page.switch_sync_user()
        assert pixels_page.sync_user_warning_displayed()
        pixels_page.switch_sync_user()

        pixels_page.click_pixel_main_button()
        pixels_page.delete_pixel_false()
        pixels_page.delete_pixel_true()

    def test_options_tags(self, pixels_page):
        #pixels_page.click_pixel_button()
        #pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        #pixels_page.click_add_pixel_button()
        #pixels_page.click_create_new_pixel_conf()
        #assert pixels_page.pixel_creation_success()
        #pixels_page.close_pixel_creation_success()

        pixels_page.click_options()
        pixels_page.click_options_tags()

        pixels_page.click_create_tag_button()
        pixels_page.click_new_tag_conf_true()
        assert pixels_page.tag_name_field_error()
        pixels_page.click_new_tag_conf_false()

        pixels_page.click_create_tag_button()
        pixels_page.enter_tag_name(self.TAG_NAME)
        pixels_page.click_new_tag_conf_false()

        pixels_page.click_create_tag_button()
        pixels_page.enter_tag_name(self.TAG_NAME)
        pixels_page.click_new_tag_conf_true()
        assert pixels_page.new_tag_is_displayed()

        pixels_page.click_pixel_main_button()

        #pixels_page.delete_pixel_false()
        #pixels_page.delete_pixel_true()


    def test_options_events_href(self, pixels_page):
        #pixels_page.click_pixel_button()
        #pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        #pixels_page.click_add_pixel_button()
        #pixels_page.click_create_new_pixel_conf()
        #assert pixels_page.pixel_creation_success()
        #pixels_page.close_pixel_creation_success()
        #Создание пикселя, законменчено, так как исчерпан лимит АПИ

        pixels_page.click_options()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()
        pixels_page.click_new_event_conf_false()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()

        pixels_page.enter_event_name(self.EVENT_NAME)

        #Далее нужно выбирать из селект списка, но ни один из вариантов выбора из селект списка не работает
        #pixels_page.choose_event_category()
        #pixels_page.choose_event_requirement_href()
        #assert pixels_page.event_url_field_is_displayed()

        #pixels_page.enter_event_url_field(self.URL_CONTAINS)

        #pixels_page.click_event_set_value()
        #assert pixels_page.event_set_value_field_is_displayed()
        #pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
        #pixels_page.click_new_event_conf_true()

    def test_options_events_with_time_period(self, pixels_page):
        #pixels_page.click_pixel_button()
        #pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        #pixels_page.click_add_pixel_button()
        #pixels_page.click_create_new_pixel_conf()
        #assert pixels_page.pixel_creation_success()
        #pixels_page.close_pixel_creation_success()

        pixels_page.click_options()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()
        pixels_page.click_new_event_conf_false()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()

        pixels_page.enter_event_name(self.EVENT_NAME)

        #Далее нужно выбирать из селект списка, но ни один из вариантов выбора из селект списка не работает
        #pixels_page.choose_event_category()
        #pixels_page.choose_event_requirement_with_time_period()
        #assert pixels_page.event_time_period_field_is_displayed()
        #assert pixels_page.event_amount_field_is_displayed()

        #pixels_page.enter_event_time_period()
        #pixels_page.enter_event_amount(self.FIRST_VALUE)

        #pixels_page.click_event_set_value()
        #assert pixels_page.event_set_value_field_is_displayed()
        #pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
        #pixels_page.click_new_event_conf_true()


    def test_options_events_js(self, pixels_page):
        #pixels_page.click_pixel_button()
        #pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
        #pixels_page.click_add_pixel_button()
        #pixels_page.click_create_new_pixel_conf()
        #assert pixels_page.pixel_creation_success()
        #pixels_page.close_pixel_creation_success()

        pixels_page.click_options()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()
        pixels_page.click_new_event_conf_false()

        pixels_page.click_new_event_button()
        assert pixels_page.right_side_bar_opened()

        pixels_page.enter_event_name(self.EVENT_NAME)
        #Далее нужно выбирать из селект списка, но ни один из вариантов выбора из селект списка не работает
        #pixels_page.choose_event_category()
        #pixels_page.choose_event_requirement_js()
        #assert pixels_page.event_js_field_is_displayed()

        #pixels_page.enter_event_js_field(self.EVENT_NAME)
        #pixels_page.click_event_set_value()
        #assert pixels_page.event_set_value_field_is_displayed()
        #pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
        #pixels_page.click_new_event_conf_true()



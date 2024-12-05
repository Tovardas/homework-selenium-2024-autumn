import time

import allure

from base_case import BaseCase


class TestPixelsPage(BaseCase):
    INCORRECT_DOMAIN = 'notCorrectTochkaRu'
    CORRECT_DOMAIN = "https://example.com"
    INCORRECT_ID = "123"
    INCORRECT_EMAIL = "notCorrectSobakaTochkaRu"
    NEW_NAME = "New Pixel Testing Name"
    TAG_NAME = "testing"
    EVENT_NAME = "testing event"
    URL_CONTAINS = "test/number"
    FIRST_VALUE = '3'
    JS_NAME = 'jsname'

    def test_open_catalog_modal(self, pixels_page, pixels_page_verification):
        with allure.step("Открытие модального окна пикселей"):
            pixels_page.click_pixel_button()
            pixels_page_verification.check_pixel_modal_visible()

    def test_not_correct_data(self, pixels_page, pixels_page_verification):
        with allure.step("Неверные данные для домена пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.INCORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page_verification.check_pixel_domain_error()

    def test_not_correct_pixel_id(self, pixels_page, pixels_page_verification):
        with allure.step("Неверные данные для ID пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.click_id_pixel_modal_button()
            pixels_page.enter_pixel_id_info(self.INCORRECT_ID, self.INCORRECT_EMAIL)
            pixels_page.click_add_pixel_button()
            pixels_page_verification.check_pixel_email_error()

    def test_correct_data(self, pixels_page, pixels_page_verification):
        with allure.step("Корректные данные для домена пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_rename_pixel(self, pixels_page, pixels_page_verification):
        with allure.step("Переименование пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()
            pixels_page.rename_pixel_false()
            pixels_page.rename_pixel_true(self.NEW_NAME)
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_options_code_pixel(self, pixels_page, pixels_page_verification):
        with allure.step("Опции для кода пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()

            pixels_page.click_options()
            pixels_page.click_options_code_pixel()

            pixels_page.switch_auto_search()
            pixels_page.switch_auto_search()

            pixels_page.switch_data_layer()
            pixels_page_verification.check_data_layer_fields()

            pixels_page.switch_data_layer()

            pixels_page.switch_sync_user()
            pixels_page_verification.check_sync_user_warning()
            pixels_page.switch_sync_user()

            pixels_page.click_pixel_main_button()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_options_tags(self, pixels_page, pixels_page_verification):
        with allure.step("Опции для тегов пикселя"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()

            pixels_page.click_options()
            pixels_page.click_options_tags()

            with allure.step("Создание нового тега с ошибкой в имени"):
                pixels_page.click_create_tag_button()
                pixels_page.click_new_tag_conf_true()
                pixels_page_verification.check_tag_name_field_error()
                pixels_page.click_new_tag_conf_false()

            with allure.step("Создание нового тега с заполнением имени"):
                pixels_page.click_create_tag_button()
                pixels_page.enter_tag_name(self.TAG_NAME)
                pixels_page.click_new_tag_conf_false()

            with allure.step("Создание нового тега с успешным сохранением"):
                pixels_page.click_create_tag_button()
                pixels_page.enter_tag_name(self.TAG_NAME)
                pixels_page.click_new_tag_conf_true()
                pixels_page_verification.check_new_tag_displayed()

            pixels_page.click_pixel_main_button()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_options_events_href(self, pixels_page, pixels_page_verification):
        with allure.step("Опции для событий с ссылкой"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()

            pixels_page.click_options()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()
            pixels_page.click_new_event_conf_false()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()

            pixels_page.enter_event_name(self.EVENT_NAME)
            pixels_page.choose_event_category()
            pixels_page.choose_event_requirement_href()

            pixels_page_verification.check_event_url_field_displayed()
            pixels_page.enter_event_url_field(self.URL_CONTAINS)

            pixels_page.click_event_set_value()
            pixels_page_verification.check_event_set_value_field_displayed()
            pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
            pixels_page.click_new_event_conf_true()
            pixels_page.click_pixel_main_button()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_options_events_with_time_period(self, pixels_page, pixels_page_verification):
        with allure.step("Опции для событий с временным промежутком"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()

            pixels_page.click_options()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()
            pixels_page.click_new_event_conf_false()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()

            pixels_page.enter_event_name(self.EVENT_NAME)

            pixels_page.choose_event_category()
            pixels_page.choose_event_requirement_with_time_period()
            pixels_page_verification.check_event_time_period_fields()

            pixels_page.enter_event_time_period()
            pixels_page.enter_event_amount(self.FIRST_VALUE)

            pixels_page.click_event_set_value()
            pixels_page_verification.check_event_set_value_field_displayed()
            pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
            pixels_page.click_new_event_conf_true()

            pixels_page.click_pixel_main_button()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

    def test_options_events_js(self, pixels_page, pixels_page_verification):
        with allure.step("Опции для событий с JavaScript"):
            pixels_page.click_pixel_button()
            pixels_page.enter_pixel_domain(self.CORRECT_DOMAIN)
            pixels_page.click_add_pixel_button()
            pixels_page.click_create_new_pixel_conf()
            pixels_page_verification.check_pixel_creation_success()
            pixels_page.close_pixel_creation_success()

            pixels_page.click_options()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()
            pixels_page.click_new_event_conf_false()

            pixels_page.click_new_event_button()
            pixels_page_verification.check_right_side_bar_opened()

            pixels_page.enter_event_name(self.EVENT_NAME)
            pixels_page.choose_event_category()
            pixels_page.choose_event_requirement_js()

            pixels_page_verification.check_event_js_field_displayed()
            pixels_page.enter_event_js_field(self.JS_NAME)

            pixels_page.click_event_set_value()
            pixels_page_verification.check_event_set_value_field_displayed()
            pixels_page.enter_event_set_value_field(self.FIRST_VALUE)
            pixels_page.click_new_event_conf_true()

            pixels_page.click_pixel_main_button()
            pixels_page.delete_pixel_false()
            pixels_page.delete_pixel_true()

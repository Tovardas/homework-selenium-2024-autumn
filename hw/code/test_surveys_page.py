import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.surveys_page_locators import SurveysPageLocators
from base_case import BaseCase
import time
import os

FILEPATH = os.path.join(os.path.dirname(__file__), 'images/360.png')

class TestSurveysPage(BaseCase):
    locators = SurveysPageLocators()

# ======= Положительные кейсы =======

    def test_upload_image(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.upload_image(FILEPATH)
        assert surveys_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)

        surveys_page.delete_all_from_media_library()

    def test_fill_singl_2_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_singl_2_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_singl_2_ans_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_singl_3_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.fill_2_answer_3('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_singl_3_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('a')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.fill_2_answer_3('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_singl_3_ans_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('1')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.fill_2_answer_3('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_mult_2_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_mult_2_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_mult_2_ans_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_mult_3_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.fill_2_answer_3('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_mult_3_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('a')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.fill_2_answer_3('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_mult_3_ans_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('1')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.fill_2_answer_3('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_user_input_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_user_input_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_user_input_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_scale_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_scale_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_scale_num(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_3_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.fill_2_answer_3('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.fill_2_answer_3('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_3_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('a')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.fill_2_answer_3('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('a')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.fill_2_answer_3('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_3_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('1')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.fill_2_answer_3('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('1')
        surveys_page.click_add_answer()
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.fill_2_answer_3('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_with_link_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('ф')
        surveys_page.fill_2_answer_1('ф')
        surveys_page.fill_2_answer_2('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('ф')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('ф')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('ф')
        surveys_page.fill_3_description('ф')
        surveys_page.click_3_add_link()
        surveys_page.fill_3_link('http://aboba.ru')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'ф'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_eng(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.fill_2_answer_2('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('a')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('a')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a')
        surveys_page.fill_3_description('a')
        surveys_page.fill_3_link('http://aboba.ru')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'

        surveys_page.remove_lead_form()

    def test_fill_all_questions_2_ans_rus(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.click_last_image_name_from_media_library()

        surveys_page.fill_1_compact_all_data('1', '1', '1', '1')
        surveys_page.click_continue()
        
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_many()
        surveys_page.fill_2_title('1')
        surveys_page.fill_2_answer_1('1')
        surveys_page.fill_2_answer_2('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_answer()
        surveys_page.fill_2_title('1')
        surveys_page.click_add_question()
        surveys_page.click_2_selector_scale()
        surveys_page.fill_2_title('1')
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('1')
        surveys_page.fill_3_description('1')
        surveys_page.fill_3_link('http://aboba.ru')
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == '1'

        surveys_page.remove_lead_form()

# ======= Отрицательные кейсы =======

    def test_1_empty_all(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.empty_1_compact_all_data()
        surveys_page.click_continue()

        name_error = self.find(self.locators.ERROR_1_TITLE)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADER)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Обязательное поле'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def test_1_errors_all(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*256, 'a'*31, 'a'*51, 'a'*351)
        surveys_page.click_continue()

        name_error = self.find(self.locators.ERROR_1_TITLE)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADER)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Превышена максимальная длина поля'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def test_2_question_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.click_continue()
        self.find(self.locators.ERROR_2_QUESTION)

        surveys_page.click_continue()
        surveys_page.fill_2_title('a')
        self.find(self.locators.ERROR_2_QUESTION)

        surveys_page.click_continue()
        surveys_page.fill_2_answer_1('a')
        self.find(self.locators.ERROR_2_QUESTION)

    def test_2_question_empty_many(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.click_2_selector_many()

        surveys_page.click_continue()
        self.find(self.locators.ERROR_2_QUESTION)

        surveys_page.click_continue()
        surveys_page.fill_2_title('a')
        self.find(self.locators.ERROR_2_QUESTION)

        surveys_page.click_continue()
        surveys_page.fill_2_answer_1('a')
        self.find(self.locators.ERROR_2_QUESTION)

    def test_2_question_empty_answer(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.click_2_selector_answer()

        surveys_page.click_continue()
        self.find(self.locators.ERROR_2_QUESTION)

    def test_2_question_empty_scale(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.click_2_selector_scale()

        surveys_page.click_continue()
        self.find(self.locators.ERROR_2_QUESTION)

    def test_2_add_stop(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.click_2_add_stop()

        surveys_page.fill_2_stop_header('a')
        surveys_page.fill_2_stop_description('a')
        surveys_page.click_continue()
        surveys_page.click_continue()

        assert surveys_page.get_form_name() == 'a'*10

        surveys_page.remove_lead_form()

    def test_3_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.fill_2_answer_1('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.empty_3_all()
        surveys_page.click_continue()

        name_error = self.find(self.locators.ERROR_3_HEADER)
        desc_error = self.find(self.locators.ERROR_3_DESCRIPTION)

        expected_message = 'Обязательное поле'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert desc_error.text == expected_message, f"Expected '{expected_message}', got '{desc_error.text}'"

    def test_3_over(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a'*26)
        surveys_page.fill_3_description('a'*161)
        surveys_page.click_continue()

        name_error = self.find(self.locators.ERROR_3_HEADER)
        desc_error = self.find(self.locators.ERROR_3_DESCRIPTION)

        expected_message = 'Превышена максимальная длина поля'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert desc_error.text == expected_message, f"Expected '{expected_message}', got '{desc_error.text}'"

    def test_3_link(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)

        surveys_page.click_last_image_name_from_media_library()
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.click_3_add_link()

        surveys_page.fill_3_link('ht')
        surveys_page.click_continue()

        link_error = self.find(self.locators.ERROR_3_LINK)

        expected_message = 'Необходимо указать протокол http(s)'
        assert link_error.text == expected_message, f"Expected '{expected_message}', got '{link_error.text}'"

        surveys_page.fill_3_link('tp://')
        surveys_page.click_continue()

        expected_message = 'Невалидный url'
        assert link_error.text == expected_message, f"Expected '{expected_message}', got '{link_error.text}'"

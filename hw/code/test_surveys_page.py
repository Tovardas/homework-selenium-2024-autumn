import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
import time
import os

FILEPATH = os.path.join(os.path.dirname(__file__), 'images/nya.png')

SURVEY_NAME = 'SURVEY_NAME'
SURVEY_COMPANY_NAME = 'SURVEY_COMPANY_NAME'
SURVEY_TITLE = 'SURVEY_TITLE'
SURVEY_DESCRIPTION = 'SURVEY_DESCRIPTION'

class TestSurveysPage(BaseCase):
    def test_upload_image(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.upload_image(FILEPATH)
        assert surveys_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)
        surveys_page.delete_all_from_media_library()

    def test_1_empty_all(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.empty_1_compact_all_data()
        surveys_page.click_continue()
        surveys_page.check_1_errors_empty('Обязательное поле')

    def test_1_errors_all(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*256, 'a'*31, 'a'*51, 'a'*351)
        surveys_page.click_continue()
        surveys_page.check_1_errors_all('Превышена максимальная длина поля')

    def test_2_question_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.click_continue()
        surveys_page.check_2_error_empty()

        surveys_page.click_continue()
        surveys_page.fill_2_title('a')
        surveys_page.check_2_error_empty()

        surveys_page.click_continue()
        surveys_page.fill_2_answer_1('a')
        surveys_page.check_2_error_empty()

    def test_2_question_empty_many(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.click_2_selector_many()

        surveys_page.click_continue()
        surveys_page.check_2_error_empty()

        surveys_page.click_continue()
        surveys_page.fill_2_title('a')
        surveys_page.check_2_error_empty()

        surveys_page.click_continue()
        surveys_page.fill_2_answer_1('a')
        surveys_page.check_2_error_empty()

    def test_2_question_empty_answer(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.click_2_selector_answer()

        surveys_page.click_continue()
        surveys_page.check_2_error_empty()

    def test_2_question_empty_scale(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.click_2_selector_scale()

        surveys_page.click_continue()
        surveys_page.check_2_error_empty()

    def test_2_add_stop(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.click_2_add_stop()

        surveys_page.fill_2_stop_header('a')
        surveys_page.fill_2_stop_description('a')

    def test_3_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.empty_3_all()
        surveys_page.click_continue()
        surveys_page.check_3_error_empty('Обязательное поле')

    def test_3_over(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.fill_3_thanks('a'*26)
        surveys_page.fill_3_description('a'*161)
        surveys_page.click_continue()
        surveys_page.check_3_errors_all('Превышена максимальная длина поля')

    def test_3_link(self, surveys_page):
        surveys_page.click_create_surveys_button()
        surveys_page.fill_1_compact_all_data('a'*10, 'a'*10, 'a'*10, 'a'*10)
        surveys_page.upload_image(FILEPATH)
        time.sleep(10)
        surveys_page.click_continue()

        surveys_page.fill_2_title('a')
        surveys_page.click_2_selector_answer()
        surveys_page.click_continue()

        surveys_page.click_3_add_link()

        surveys_page.fill_3_link('ht')
        surveys_page.click_continue()
        surveys_page.check_3_errors_link('Необходимо указать протокол http(s)')

        surveys_page.fill_3_link('tp://')
        surveys_page.click_continue()
        surveys_page.check_3_errors_link('Невалидный url')

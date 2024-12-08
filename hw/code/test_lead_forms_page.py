import os
import pytest
import time
from ui.locators.lead_forms_locators import LeadFormsPageLocators
from base_case import BaseCase

FILEPATH = os.path.join(os.path.dirname(__file__), 'images/360.jpg')

class TestLeadFormsPage(BaseCase):
    locators = LeadFormsPageLocators()

# ======= Положительные кейсы =======

    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.delete_all_from_media_library()
        assert leadforms_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)

        leadforms_page.delete_all_from_media_library()

    def test_create_compact_empty_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_empty_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_empty_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_more_text_empty_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_more_text()
        leadforms_page.fill_1_more_text_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_more_text_empty_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_more_text()
        leadforms_page.fill_1_more_text_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_more_text_empty_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_more_text()
        leadforms_page.fill_1_more_text_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_magnet_rub_empty_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_magnet_rub_empty_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_magnet_rub_empty_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_magnet_percent_empty_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_sale_percent()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_magnet_percent_empty_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_sale_percent()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_magnet_percent_empty_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_sale_percent()
        leadforms_page.fill_1_magnet_sale(50)
        leadforms_page.fill_1_without_desc_data('1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_magnet_bonus_empty_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_bonus()
        leadforms_page.fill_1_magnet_bonus('ф')
        leadforms_page.fill_1_without_desc_data('ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_magnet_percent_empty_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_bonus()
        leadforms_page.fill_1_magnet_bonus('a')
        leadforms_page.fill_1_without_desc_data('a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_magnet_percent_empty_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_bonus()
        leadforms_page.fill_1_magnet_bonus('1')
        leadforms_page.fill_1_without_desc_data('1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_name_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_phone_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_email_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_link_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_birthday_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_city_contact(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_all_contacts(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        time.sleep(1)
        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_2_ans_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_2_ans_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_2_ans_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_3_ans_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_3_ans_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_singl_3_ans_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_2_ans_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_2_ans_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_2_ans_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_3_ans_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_3_ans_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_mult_3_ans_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.click_add_answer()
        leadforms_page.fill_2_answer_3('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_user_ans_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_user_ans_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_question_user_ans_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_all_questions(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_site_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_site_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_site_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_phone_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_phone_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_phone_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_promocode_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_promocode_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('a')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_promocode_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('1')
        leadforms_page.continue_1()

        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_notifications_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_notifications_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_with_notifications_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

    def test_create_compact_all_fields_rus(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.continue_1()
        
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('ф')
        leadforms_page.fill_2_answer_1('ф')
        leadforms_page.fill_2_answer_2('ф')
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('ф')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('ф')
        leadforms_page.fill_3_description('ф')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('ф')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('ф')
        leadforms_page.fill_4_address('ф')
        leadforms_page.fill_4_email('aboba@mail.ru')
        leadforms_page.fill_4_inn('ф')
        
        assert leadforms_page.get_form_name() == 'ф'

        leadforms_page.remove_lead_form()

    def test_create_compact_all_fields_eng(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        leadforms_page.fill_1_compact_all_data('a', 'a', 'a', 'a')
        leadforms_page.continue_1()
        
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('a')
        leadforms_page.fill_2_answer_1('a')
        leadforms_page.fill_2_answer_2('a')
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('a')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('a')
        leadforms_page.fill_3_description('a')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('a')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('a')
        leadforms_page.fill_4_address('a')
        leadforms_page.fill_4_email('aboba@mail.ru')
        leadforms_page.fill_4_inn('a')
        
        assert leadforms_page.get_form_name() == 'a'

        leadforms_page.remove_lead_form()

    def test_create_compact_all_fields_num(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        time.sleep(1)
        leadforms_page.fill_1_compact_all_data('1', '1', '1', '1')
        leadforms_page.continue_1()
        
        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.create_question_2()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.create_question_2()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.fill_2_answer_1('1')
        leadforms_page.fill_2_answer_2('1')
        leadforms_page.create_question_2()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_2_question('1')
        leadforms_page.continue_1()

        leadforms_page.fill_3_header('1')
        leadforms_page.fill_3_description('1')
        leadforms_page.click_3_site()
        leadforms_page.fill_3_site('http://aboba.ru')
        leadforms_page.click_3_phone()
        leadforms_page.fill_3_phone('+77777777777')
        leadforms_page.click_3_promocode()
        leadforms_page.fill_3_promocode('1')
        leadforms_page.continue_1()

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('aboba@mail.ru')
        leadforms_page.fill_4_name('1')
        leadforms_page.fill_4_address('1')
        leadforms_page.fill_4_email('aboba@mail.ru')
        leadforms_page.fill_4_inn('1')
        leadforms_page.continue_1()
    
        assert leadforms_page.get_form_name() == '1'

        leadforms_page.remove_lead_form()

# ======= Отрицательные кейсы =======

    def test_error_1_compact_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.empty_1_compact_all_data()
        leadforms_page.continue_1()

        logo_empty = self.find(self.locators.ERROR_1_LOGO)
        company_name_empty = self.find(self.locators.ERROR_1_COMPANY)
        title_empty = self.find(self.locators.ERROR_1_HEADING)
        description_empty = self.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Обязательное поле'
        assert logo_empty.text == expected_message, f"Expected '{expected_message}', got '{logo_empty.text}'"
        assert company_name_empty.text == expected_message, f"Expected '{expected_message}', got '{company_name_empty.text}'"
        assert title_empty.text == expected_message, f"Expected '{expected_message}', got '{title_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def test_error_1_compact_max_length(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_1_compact_all_data('a'*256, 'a'*31, 'a'*51, 'a'*36)
        leadforms_page.continue_1()
        
        leadform_name_error = self.find(self.locators.ERROR_1_NAME)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADING)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Обязательное поле'
        assert leadform_name_error.text == expected_message, f"Expected '{expected_message}', got '{leadform_name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def test_error_1_more_text_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_more_text()
        leadforms_page.empty_1_more_text_data()
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_MORE_TEXT)

        expected_message = 'Обязательное поле'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def test_error_1_more_text_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_more_text()
        leadforms_page.fill_1_more_text_data('a'*351)
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_MORE_TEXT)

        expected_message = 'Превышена максимальная длина поля'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def test_error_1_magnet_bonus_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_bonus()
        
        leadforms_page.empty_1_magnet_bonus()
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_BONUS)

        expected_message = 'Обязательное поле'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"
        
        leadforms_page.fill_1_magnet_bonus('a'*31)
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_BONUS)

        expected_message = 'Превышена максимальная длина поля'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"
  
    def test_error_1_magnet_sale_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_sale()
        
        leadforms_page.fill_1_magnet_sale(0)
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_SALE_ZERO)

        expected_message = 'Значение должно быть больше нуля'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"
        
        leadforms_page.click_1_magnet_sale_percent()
        leadforms_page.fill_1_magnet_sale(101)
        leadforms_page.continue_1()

        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_SALE_OVER)

        expected_message = 'Укажите скидку не больше 100%'
        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def test_error_2_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_1()

        leadforms_page.create_question_2()
        leadforms_page.continue_1()
        self.find(self.locators.ERROR_2_QUESTION)

        leadforms_page.fill_2_question('a'*3)
        leadforms_page.continue_1()
        self.find(self.locators.ERROR_2_QUESTION)

        leadforms_page.fill_2_answer_1('a'*3)
        leadforms_page.continue_1()
        self.find(self.locators.ERROR_2_QUESTION)

    def test_error_2_contacts_error(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_1()

        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()

        error = self.find(self.locators.ERROR_2_CONTACT)
        
        expected_message = 'Минимальное количество полей: 1'
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def test_error_3_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.empty_3_header()
        leadforms_page.continue_1()

        heading_empty = self.find(self.locators.ERROR_3_HEADING)

        expected_message = 'Обязательное поле'
        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"

        leadforms_page.fill_3_header('a'*26)
        leadforms_page.fill_3_description('a'*161)
        leadforms_page.continue_1()

        heading_empty = self.find(self.locators.ERROR_3_HEADING)
        description_empty = self.find(self.locators.ERROR_3_DESCRIPTION)

        expected_message = 'Превышена максимальная длина поля'
        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def test_error_3_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.click_3_site()
        leadforms_page.click_3_phone()
        leadforms_page.click_3_promocode()

        leadforms_page.fill_3_site('a')
        leadforms_page.fill_3_phone('a')
        leadforms_page.fill_3_promocode('a'*31)
        leadforms_page.continue_1()

        site_input = self.find(self.locators.ERROR_3_SITE)

        expected_message = 'Невалидный url'
        assert site_input.text == expected_message, f"Expected '{expected_message}', got '{site_input.text}'"

        phone_input = self.find(self.locators.ERROR_3_PHONE)

        expected_message = 'Телефон должен начинаться с + и содержать только цифры'
        assert phone_input.text == expected_message, f"Expected '{expected_message}', got '{phone_input.text}'"

        promocode_input = self.find(self.locators.ERROR_3_PROMO)

        expected_message = 'Превышена максимальная длина поля'
        assert promocode_input.text == expected_message, f"Expected '{expected_message}', got '{promocode_input.text}'"

    def test_error_4_empty_len(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_1()
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.empty_4_name()
        leadforms_page.empty_4_address()
        leadforms_page.continue_1()

        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)

        expected_message = 'Обязательное поле'
        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"

        leadforms_page.fill_4_name('a'*256)
        leadforms_page.fill_4_address('a'*256)
        leadforms_page.fill_4_inn('a'*33)
        leadforms_page.continue_1()

        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)

        expected_message = 'Превышена максимальная длина поля'
        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"

        leadforms_page.fill_4_email('a')

        email_input = self.find(self.locators.ERROR_4_EMAIL)

        expected_message = 'Некорректный email адрес'
        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('a')
        leadforms_page.continue_1()

        email_input = self.find(self.locators.ERROR_4_NOTIFY_EMAIL)

        expected_message = 'Поле содержит невалидный email адрес'
        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"

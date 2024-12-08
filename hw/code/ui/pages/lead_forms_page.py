from ui.pages.base_page import BasePage
import time
from ui.locators.lead_forms_locators import LeadFormsPageLocators
from selenium.webdriver.support import expected_conditions as ec


class LeadFormsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormsPageLocators()

    DEFAULT_ANSWERS_COUNT = 2
    CONTACT_INFO_TYPES_AND_PLACEHOLDERS = {
        'Фамилия': 'Введите фамилию',
        'Электронная почта': 'Введите email',
        'Возраст': 'Введите возраст'
    }

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def click_last_image_name_from_media_library(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME)

    def delete_all_from_media_library(self):
        self.click(self.locators.EDIT_IMAGES_BUTTON)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON)
        self.click(self.locators.DELETE_IMAGES_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def continue_1(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def empty_1_compact_all_data(self):
        name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()

    def fill_1_compact_all_data(self, name, company, title, description):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        leadform_name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()
        leadform_name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)
        description_input.send_keys(description)

    def fill_1_more_text_all_data(self, name, company, title, description):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.MORE_TEXT_INPUT)
        leadform_name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()
        leadform_name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)
        description_input.send_keys(description)

    def fill_1_without_desc_data(self, name, company, title):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        leadform_name_input.clear()
        company_name_input.clear()
        title_input.clear()
        leadform_name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)

    def check_empty_1_compact_all(self, expected_message):
        logo_empty = self.find(self.locators.ERROR_1_LOGO)
        company_name_empty = self.find(self.locators.ERROR_1_COMPANY)
        title_empty = self.find(self.locators.ERROR_1_HEADING)
        description_empty = self.find(self.locators.ERROR_1_DESCRIPTION)

        assert logo_empty.text == expected_message, f"Expected '{expected_message}', got '{logo_empty.text}'"
        assert company_name_empty.text == expected_message, f"Expected '{expected_message}', got '{company_name_empty.text}'"
        assert title_empty.text == expected_message, f"Expected '{expected_message}', got '{title_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def check_errors_1_compact_all(self, expected_message):
        leadform_name_error = self.find(self.locators.ERROR_1_NAME)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADING)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        assert leadform_name_error.text == expected_message, f"Expected '{expected_message}', got '{leadform_name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def click_1_more_text(self):
        self.click(self.locators.MORE_TEXT_BUTTON)

    def click_1_magnet(self):
        self.click(self.locators.MAGNET_BUTTON)

    def click_1_magnet_bonus(self):
        self.click(self.locators.MAGNET_BONUS_BUTTON)

    def click_1_magnet_sale(self):
        self.click(self.locators.MAGNET_SALE_BUTTON)

    def click_1_magnet_sale_percent(self):
        self.click(self.locators.MAGNET_SALE_PERCENT_BUTTON)

    def empty_1_more_text_data(self):
        more_text_input = self.find(self.locators.MORE_TEXT_INPUT)
        more_text_input.clear()

    def fill_1_more_text_data(self, text):
        more_text_input = self.find(self.locators.MORE_TEXT_INPUT)
        more_text_input.send_keys(text)

    def check_empty_1_more_text(self, expected_message):
        more_text_empty = self.find(self.locators.ERROR_MORE_TEXT)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def check_error_1_more_text(self, expected_message):
        more_text_empty = self.find(self.locators.ERROR_MORE_TEXT)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def empty_1_magnet_bonus(self):
        more_text_input = self.find(self.locators.MAGNET_BONUS_INPUT)
        more_text_input.clear()

    def fill_1_magnet_bonus(self, text):
        more_text_input = self.find(self.locators.MAGNET_BONUS_INPUT)
        more_text_input.send_keys(text)

    def check_empty_1_magnet_bonus(self, expected_message):
        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_BONUS)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def check_error_1_magnet_bonus(self, expected_message):
        time.sleep(1)
        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_BONUS)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def fill_1_magnet_sale(self, text):
        time.sleep(1)
        more_text_input = self.find(self.locators.MAGNET_SALE_INPUT)
        more_text_input.clear()
        more_text_input.send_keys(text)

    def check_zero_1_magnet_sale(self, expected_message):
        time.sleep(1)
        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_SALE_ZERO)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def check_over_1_magnet_sale(self, expected_message):
        time.sleep(1)
        more_text_empty = self.find(self.locators.ERROR_1_MAGNET_SALE_OVER)

        assert more_text_empty.text == expected_message, f"Expected '{expected_message}', got '{more_text_empty.text}'"

    def fill_form_1(self):
        time.sleep(1)
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        leadform_name_input.send_keys('a'*10)
        company_name_input.send_keys('a'*10)
        title_input.send_keys('a'*10)
        description_input.send_keys('a'*10)

    def create_question_2(self):
        time.sleep(1)
        self.click(self.locators.ADD_QUESTION_BUTTON)

    def fill_2_question(self, description):
        question_input = self.find(self.locators.QUESTION_INPUT)
        question_input.send_keys(description)

    def fill_2_answer_1(self, description):
        answer_input = self.find(self.locators.ANSWER_1_INPUT)
        answer_input.send_keys(description)

    def fill_2_answer_2(self, description):
        answer_input = self.find(self.locators.ANSWER_2_INPUT)
        answer_input.send_keys(description)

    def fill_2_answer_3(self, description):
        answer_input = self.find(self.locators.ANSWER_3_INPUT)
        answer_input.send_keys(description)

    def click_add_answer(self):
        self.click(self.locators.ADD_ANSWER_BUTTON)

    def click_add_contact_data(self):
        self.click(self.locators.ADD_CONTACT_BUTTON)
    
    def click_multiple_answers_question(self):
        self.click(self.locators.SELECT_QUESTION_TYPE_BUTTON)
        self.click(self.locators.MULTIPLE_ANSWERS_BUTTON)

    def click_user_input_question(self):
        self.click(self.locators.SELECT_QUESTION_TYPE_BUTTON)
        self.click(self.locators.USER_ANSWER_BUTTON)

    def click_add_name_contact(self):
        self.click(self.locators.NAME_CONTACT)
    
    def click_add_phone_contact(self):
        self.click(self.locators.PHONE_CONTACT)
    
    def click_add_email_contact(self):
        self.click(self.locators.EMAIL_CONTACT)
    
    def click_add_link_contact(self):
        self.click(self.locators.LINK_CONTACT)
    
    def click_add_birthday_contact(self):
        self.click(self.locators.BIRTHDAY_CONTACT)
    
    def click_add_city_contact(self):
        self.click(self.locators.CITY_CONTACT)

    def click_add_selected_contacts(self):
        self.click(self.locators.ADD_SELECTED_CONTACTS_BUTTON)

    def click_2_bin_name(self):
        self.click(self.locators.BIN_NAME_BUTTON)

    def click_2_bin_phone(self):
        self.click(self.locators.BIN_PHONE_BUTTON)

    def check_question_2_error(self):
        time.sleep(1)
        self.find(self.locators.ERROR_2_QUESTION)

    def check_error_2_contacts(self, expected_message):
        error = self.find(self.locators.ERROR_2_CONTACT)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def empty_3_header(self):
        time.sleep(1)
        heading_input = self.find(self.locators.HEADING_INPUT)
        heading_input.clear()

    def fill_3_header(self, header):
        answer_input = self.find(self.locators.HEADING_INPUT)
        answer_input.clear()
        answer_input.send_keys(header)

    def fill_3_description(self, description):
        answer_input = self.find(self.locators.DESCRIPTION_3_INPUT)
        answer_input.clear()
        answer_input.send_keys(description)

    def check_empty_3_heading(self, expected_message):
        time.sleep(1)
        heading_empty = self.find(self.locators.ERROR_3_HEADING)

        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"

    def check_errors_3_heading(self, expected_message):
        time.sleep(1)
        heading_empty = self.find(self.locators.ERROR_3_HEADING)
        description_empty = self.find(self.locators.ERROR_3_DESCRIPTION)

        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def click_3_site(self):
        self.click(self.locators.SITE_BUTTON)

    def click_3_phone(self):
        self.click(self.locators.PHONE_BUTTON)
        
    def click_3_promocode(self):
        self.click(self.locators.PROMOCODE_BUTTON)

    def fill_3_site(self, site):
        site_input = self.find(self.locators.SITE_INPUT)
        site_input.send_keys(site)

    def fill_3_phone(self, phone):
        phone_input = self.find(self.locators.PHONE_INPUT)
        phone_input.send_keys(phone)

    def fill_3_promocode(self, promocode):
        promocode_input = self.find(self.locators.PROMOCODE_INPUT)
        promocode_input.send_keys(promocode)

    def check_errors_3_site(self, expected_message):
        time.sleep(1)
        site_input = self.find(self.locators.ERROR_3_SITE)

        assert site_input.text == expected_message, f"Expected '{expected_message}', got '{site_input.text}'"

    def check_errors_3_phone(self, expected_message):
        time.sleep(1)
        phone_input = self.find(self.locators.ERROR_3_PHONE)

        assert phone_input.text == expected_message, f"Expected '{expected_message}', got '{phone_input.text}'"

    def check_errors_3_promocode(self, expected_message):
        time.sleep(1)
        promocode_input = self.find(self.locators.ERROR_3_PROMO)

        assert promocode_input.text == expected_message, f"Expected '{expected_message}', got '{promocode_input.text}'"

    def click_4_notify(self):
        self.click(self.locators.NOTIFY_EMAIL_BUTTON)

    def empty_4_name(self):
        time.sleep(1)
        name_input = self.find(self.locators.NAME_4_INPUT)
        name_input.clear()

    def empty_4_address(self):
        time.sleep(1)
        address_input = self.find(self.locators.ADDRESS_INPUT)
        address_input.clear()

    def empty_4_email(self):
        time.sleep(1)
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.clear()

    def fill_4_name(self, name):
        name_input = self.find(self.locators.NAME_4_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    def fill_4_address(self, address):
        address_input = self.find(self.locators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(address)

    def fill_4_email(self, email):
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def fill_4_notify_email(self, email):
        email_input = self.find(self.locators.NOTIFY_EMAIL_INPUT)
        email_input.send_keys(email)
        
    def fill_4_inn(self, inn):
        inn_input = self.find(self.locators.INN_INPUT)
        inn_input.send_keys(inn)

    def check_4_errors_empty(self, expected_message):
        time.sleep(1)
        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)

        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"

    def check_4_errors_len(self, expected_message):
        time.sleep(1)
        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)
        inn_input = self.find(self.locators.ERROR_4_INN)

        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"
        assert inn_input.text == expected_message, f"Expected '{expected_message}', got '{inn_input.text}'"

    def check_4_error_email(self, expected_message):
        time.sleep(1)
        email_input = self.find(self.locators.ERROR_4_EMAIL)

        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"

    def check_4_error_notify_email(self, expected_message):
        time.sleep(1)
        email_input = self.find(self.locators.ERROR_4_NOTIFY_EMAIL)

        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"

    def get_form_name(self) -> str:
        name = self.find(self.locators.FIRST_LEAD_FORM_NAME)
        return name.text

    def remove_lead_form(self):
        self.click(self.locators.ARCHIVE_BUTTON)
        self.click(self.locators.ARCHIVE_ACCEPT_BUTTON)

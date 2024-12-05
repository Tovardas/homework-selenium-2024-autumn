from ui.pages.base_page import BasePage
from selenium.webdriver import Keys
from ui.locators.surveys_page_locators import SurveysPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

class SurveysPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/surveys'
    locators = SurveysPageLocators()

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_create_surveys_button(self):
        self.click(self.locators.CREATE_SURVEY_BUTTON)

    def empty_1_compact_all_data(self):
        time.sleep(1)
        name_input = self.find(self.locators.TITLE_INPUT)
        company_name_input = self.find(self.locators.COMPANY_INPUT)
        title_input = self.find(self.locators.HEADER_INPUT)
        description_input = self.find(self.locators.DESCRIPTION_INPUT)
        name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()

    def fill_1_compact_all_data(self, name, company, title, desc):
        time.sleep(1)
        name_input = self.find(self.locators.TITLE_INPUT)
        company_name_input = self.find(self.locators.COMPANY_INPUT)
        title_input = self.find(self.locators.HEADER_INPUT)
        description_input = self.find(self.locators.DESCRIPTION_INPUT)
        name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)
        description_input.send_keys(desc)

    def check_1_errors_empty(self, expected_message):
        name_error = self.find(self.locators.ERROR_1_TITLE)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADER)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def check_1_errors_all(self, expected_message):
        name_error = self.find(self.locators.ERROR_1_TITLE)
        company_name_error = self.find(self.locators.ERROR_1_COMPANY)
        title_error = self.find(self.locators.ERROR_1_HEADER)
        description_error = self.find(self.locators.ERROR_1_DESCRIPTION)

        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def delete_all_from_media_library(self):
        self.click(self.locators.EDIT_IMAGES_BUTTON)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON)
        self.click(self.locators.DELETE_IMAGES_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def fill_2_title(self, title):
        title_input = self.find(self.locators.QUESTION_TITLE_INPUT)
        title_input.send_keys(title)
        
    def fill_2_answer_1(self, answer):
        answer_input = self.find(self.locators.ANSWER_1_INPUT)
        answer_input.send_keys(answer)

    def fill_2_answer_2(self, answer):
        answer_input = self.find(self.locators.ANSWER_2_INPUT)
        answer_input.send_keys(answer)

    def check_2_error_empty(self):
        time.sleep(1)
        self.find(self.locators.ERROR_2_QUESTION)

    def click_2_selector_many(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_MANY)

    def click_2_selector_answer(self):
        self.click(self.locators.SELECTOR_INPUT)
        time.sleep(1)
        self.click(self.locators.SELECTOR_ANSWER)

    def click_2_selector_scale(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_SCALE)

    def click_2_add_stop(self):
        self.click(self.locators.ADD_STOP_BUTTON)

    def fill_2_stop_header(self, header):
        title_input = self.find(self.locators.STOP_HEADING_INPUT)
        title_input.send_keys(header)

    def fill_2_stop_description(self, desc):
        desc_input = self.find(self.locators.STOP_DESCRIPTION_INPUT)
        desc_input.send_keys(desc)

    def empty_3_all(self):
        thanks_input = self.find(self.locators.HEADER_3)
        description_input = self.find(self.locators.DESCRIPTION_3)
        description_input.clear()
        thanks_input.clear()

    def click_3_add_link(self):
        self.click(self.locators.ADD_LINK_BUTTON)

    def fill_3_thanks(self, thanks):
        thanks_input = self.find(self.locators.HEADER_3)
        thanks_input.send_keys(thanks)

    def fill_3_description(self, description):
        description_input = self.find(self.locators.DESCRIPTION_3)
        description_input.send_keys(description)

    def fill_3_link(self, link):
        link_input = self.find(self.locators.LINK_3)
        link_input.send_keys(link)

    def check_3_error_empty(self, expected_message):
        time.sleep(1)
        name_error = self.find(self.locators.ERROR_3_HEADER)
        desc_error = self.find(self.locators.ERROR_3_DESCRIPTION)

        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert desc_error.text == expected_message, f"Expected '{expected_message}', got '{desc_error.text}'"

    def check_3_errors_all(self, expected_message):
        time.sleep(1)
        name_error = self.find(self.locators.ERROR_3_HEADER)
        desc_error = self.find(self.locators.ERROR_3_DESCRIPTION)

        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert desc_error.text == expected_message, f"Expected '{expected_message}', got '{desc_error.text}'"

    def check_3_errors_link(self, expected_message):
        time.sleep(1)
        link_error = self.find(self.locators.ERROR_3_LINK)

        assert link_error.text == expected_message, f"Expected '{expected_message}', got '{link_error.text}'"

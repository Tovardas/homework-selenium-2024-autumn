from selenium.webdriver.ie.webdriver import WebDriver
from ui.pages.base_page import BasePage
from selenium.webdriver import Keys
from ui.locators.cases_page_locators import CasesPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC



class CasesPage(BasePage):
    locators = CasesPageLocators()

    def click_cases_button(self):
        self.click(self.locators.CASES_BUTTON)

    def click_cases_card(self):
        self.scroll_and_click(self.locators.CASES_CARD)

    def click_cases_tag(self):
        self.click(self.locators.CASES_TAG)


    def click_cases_content(self):
        self.scroll_and_click(self.locators.CASES_CONTENT_LINK)

    def header_became_visible(self) -> bool:
        return self.became_visible(self.locators.CASES_CONTENT_HEADER)

    def click_cases_cabinet_button(self):
        self.scroll_and_click(self.locators.CASES_CABINET_NAME)

    def click_pagination_number(self):
        self.scroll_and_click(self.locators.CASES_PAGINATION_NUMBER)

    def click_pagination_left(self):
        self.scroll_and_click(self.locators.CASES_PAGINATION_LEFT)

    def click_pagination_right(self):
        self.scroll_and_click(self.locators.CASES_PAGINATION_RIGHT)



import time
from urllib.parse import urlparse, parse_qs

from selenium.webdriver.support.ui import WebDriverWait
from ui.locators.cases_page_locators import CasesPageLocators
from ui.pages.base_page import BasePage
from ui.pages.base_page import PageNotOpenedException


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

    def query_parameter_matches(self, parameter, value, timeout=None):
        if timeout is None:
            timeout = 5

        def parameters_match(driver):
            current_url = driver.current_url
            parsed_url = urlparse(current_url)
            query_params = parse_qs(parsed_url.query)
            expected_params = {parameter: [str(value)]}
            return query_params == expected_params

        try:
            WebDriverWait(self.driver, timeout).until(parameters_match)
            return True
        except:
            raise PageNotOpenedException(
                f"Не удалось найти параметр '{parameter}={value}' в URL за {timeout} секунд. Текущий URL: {self.driver.current_url}"
            )

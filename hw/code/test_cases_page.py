import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
import time

class TestCasesPage(BaseCase):
    def test_href_to_cases(self, cases_page):
        cases_page.click_cases_button()
        assert self.is_opened('https://ads.vk.com/cases')

    def test_cases_tags_redirect(self, cases_page):
        cases_page.click_cases_button()
        assert self.is_opened('https://ads.vk.com/cases')
        cases_page.click_cases_card()
        assert self.is_opened('https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king')
        cases_page.click_cases_tag()
        assert self.is_opened('https://ads.vk.com/tags/retargeting')

    def test_cases_content(self, cases_page):
        cases_page.click_cases_button()
        assert self.is_opened('https://ads.vk.com/cases')
        cases_page.click_cases_card()
        assert self.is_opened('https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king')
        cases_page.click_cases_content()
        assert cases_page.header_became_visible()
        assert self.is_opened('https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king#results')
        cases_page.click_cases_cabinet_button()
        cases_page.go_to_new_tab()
        assert self.driver.current_url.startswith("https://id.vk.com/auth")

    def test_cases_paginator(self, cases_page):
        cases_page.click_cases_button()
        assert self.is_opened('https://ads.vk.com/cases')
        cases_page.click_pagination_number()
        assert self.query_parameter_matches('p', 3)
        cases_page.click_pagination_right()
        assert self.query_parameter_matches('p', 4)
        cases_page.click_pagination_left()
        assert self.query_parameter_matches('p', 3)





import allure

from base_case import BaseCase


class TestCasesPage(BaseCase):
    @allure.title("Проверка перехода по ссылке в раздел кейсов")
    def test_href_to_cases(self, cases_page, cases_page_verification):
        with allure.step("Переходим по ссылке в раздел кейсов и проверяем редирект"):
            cases_page.click_cases_button()
            cases_page_verification.check_url_opened(cases_page.driver.current_url, 'https://ads.vk.com/cases')

    @allure.title("Проверка редиректа по тегам кейсов")
    def test_cases_tags_redirect(self, cases_page, cases_page_verification):
        with allure.step("Переходим в раздел кейсов, открываем карточку и проверяем редирект по тегам"):
            cases_page.click_cases_button()
            cases_page_verification.check_url_opened(cases_page.driver.current_url, 'https://ads.vk.com/cases')
            cases_page.click_cases_card()
            cases_page_verification.check_url_opened(cases_page.driver.current_url,
                                                     'https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king')
            cases_page.click_cases_tag()
            cases_page_verification.check_url_opened(cases_page.driver.current_url,
                                                     'https://ads.vk.com/tags/retargeting')

    @allure.title("Проверка отображения контента кейса и перехода в результаты")
    def test_cases_content(self, cases_page, cases_page_verification):
        with allure.step("Открываем карточку кейса, проверяем наличие контента и редирект в результаты"):
            cases_page.click_cases_button()
            cases_page_verification.check_url_opened(cases_page.driver.current_url, 'https://ads.vk.com/cases')
            cases_page.click_cases_card()
            cases_page_verification.check_url_opened(cases_page.driver.current_url,
                                                     'https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king')
            cases_page.click_cases_content()
            cases_page_verification.check_header_visible()
            cases_page_verification.check_url_opened(cases_page.driver.current_url,
                                                     'https://ads.vk.com/cases/snizhaem-cpf-v-4-raza-kejs-burger-king#results')
            cases_page.click_cases_cabinet_button()
            cases_page.go_to_new_tab()
            cases_page_verification.check_url_opened(cases_page.driver.current_url, 'https://id.vk.com/auth')

    @allure.title("Проверка работы пагинации на странице кейсов")
    def test_cases_paginator(self, cases_page, cases_page_verification):
        with allure.step("Проверяем работу пагинации на странице кейсов"):
            cases_page.click_cases_button()
            cases_page_verification.check_url_opened(cases_page.driver.current_url, 'https://ads.vk.com/cases')
            cases_page.click_pagination_number()
            cases_page_verification.check_query_parameter('p', 3)
            cases_page.click_pagination_right()
            cases_page_verification.check_query_parameter('p', 4)
            cases_page.click_pagination_left()
            cases_page_verification.check_query_parameter('p', 3)

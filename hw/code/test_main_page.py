import time
import allure

from base_case import BaseCase


class TestMainPage(BaseCase):
    def test_change_slide(self, main_page, main_page_verification):
        with allure.step("Меняем слайд и проверяем, что заголовок слайда изменился"):
            initial_title = main_page.get_slide_title()
            main_page.change_slide()
            main_page_verification.check_slide_title_changed(initial_title)

    def test_automatic_change_slide(self, main_page, main_page_verification):
        with allure.step("Ожидаем автоматическую смену слайда и проверяем изменение заголовка"):
            initial_title = main_page.get_slide_title()
            time.sleep(7)
            main_page_verification.check_slide_title_changed(initial_title)

    def test_go_to_auth(self, main_page, main_page_verification):
        with allure.step("Переходим по кнопке в слайдере в кабинет и проверяем открытие страницы"):
            main_page.change_slide()
            main_page.click_slider_cabinet_button()
            main_page_verification.check_url_opened('https://id.vk.com/auth')

    def test_go_to_bonus_page(self, main_page, main_page_verification):
        with allure.step("Переходим по кнопке слайдера на страницу бонусов и проверяем редирект"):
            main_page.click_slider_bonus_button()
            main_page_verification.check_url_opened('https://ads.vk.com/promo/firstbonus')

    def test_go_to_cases(self, main_page, main_page_verification):
        with allure.step("Нажимаем на 'Все кейсы' и проверяем переход на страницу кейсов"):
            main_page.click_see_all()
            main_page_verification.check_url_opened('https://ads.vk.com/cases')

    def test_go_to_case_page(self, main_page, main_page_verification):
        with allure.step("Переходим по кейсу и проверяем, что открыта страница с кейсом"):
            case_title = main_page.get_case_title()
            main_page.click_case_item()
            main_page_verification.check_url_opened('https://ads.vk.com/cases')
            main_page_verification.check_case_title_in_page(case_title)

    def test_go_to_webinar(self, main_page, main_page_verification):
        with allure.step("Переходим по элементу вебинара и проверяем редирект на страницу с вебинарами"):
            main_page.click_webinar_item()
            main_page_verification.check_url_opened('https://ads.vk.com/events')

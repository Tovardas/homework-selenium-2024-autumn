import allure

from base_case import BaseCase
from ui.fixtures import partner_page


class TestPartnerPage(BaseCase):
    def test_go_to_auth(self, partner_page, partner_page_verification):
        with allure.step("Переходим в кабинет и проверяем редирект на страницу авторизации"):
            partner_page.click_cabinet_button()
            partner_page.go_to_new_tab()
            partner_page_verification.check_url_opened('https://id.vk.com/auth')

    def test_go_to_help(self, partner_page, partner_page_verification):
        with allure.step("Переходим в раздел помощи и проверяем редирект"):
            partner_page.click_help_button()
            partner_page.go_to_new_tab()
            partner_page_verification.check_url_opened('https://ads.vk.com/help')

    def test_formats(self, partner_page, partner_page_verification):
        with allure.step("Проверяем доступность форматов для приложений и сайтов"):
            partner_page.click_format_tab('Для приложений')
            partner_page_verification.check_page_contains_formats(partner_page.APP_FORMATS)

            partner_page.click_format_tab('Для сайтов')
            partner_page_verification.check_page_contains_formats(partner_page.WEBSITE_FORMATS)

    def test_submit_button_disabled_by_default(self, partner_page, partner_page_verification):
        with allure.step("Проверяем, что кнопка отправки формы отключена по умолчанию"):
            partner_page_verification.check_submit_button_disabled()

    def test_submit_button_enabled_after_filling_form(self, partner_page, partner_page_verification):
        with allure.step("Заполняем форму и проверяем, что кнопка отправки включена"):
            partner_page.enter_name_and_email('test', 'test')
            partner_page_verification.check_submit_button_enabled()

    def test_submit_message_after_submitting_form(self, partner_page, partner_page_verification):
        with allure.step("Заполняем форму, отправляем и проверяем, что сообщение об успешной отправке отображается"):
            partner_page.enter_name_and_email('test', 'test')
            partner_page.click_submit_button()
            partner_page_verification.check_submit_message_visible()

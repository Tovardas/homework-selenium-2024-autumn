import allure
import pytest

from base_case import BaseCase


class TestFooter(BaseCase):
    def test_go_to_auth(self, main_page, footer_verification):
        with allure.step("Переходим по ссылке авторизации в футере и проверяем открытие страницы"):
            main_page.click_footer_cabinet_button()
            footer_verification.check_url_opened('https://id.vk.com/auth')

    @pytest.mark.parametrize("item_name,url,open_in_new_tab", [
        ('Новости', 'https://ads.vk.com/news', False),
        ('Полезные материалы', 'https://ads.vk.com/insights', False),
        ('Мероприятия', 'https://ads.vk.com/events', False),
        ('Документы', 'https://ads.vk.com/documents', False),
        ('Обучение для бизнеса', 'https://expert.vk.com/', True),
        ('Кейсы', 'https://ads.vk.com/cases', False),
        ('Помощь', 'https://ads.vk.com/help', False),
        ('Монетизация', 'https://ads.vk.com/partner', True),
    ])
    def test_go_to_sections(self, main_page, item_name, url, open_in_new_tab, footer_verification):
        with allure.step(f"Нажимаем на элемент '{item_name}' в футере и проверяем редирект на {url}"):
            main_page.click_footer_item(item_name)
            if open_in_new_tab:
                main_page.go_to_new_tab()
            footer_verification.check_url_opened(url)

    def test_go_to_vk_business(self, main_page, footer_verification):
        with allure.step("Нажимаем на логотип VK Business и проверяем редирект"):
            main_page.click_vk_business_logo()
            main_page.go_to_new_tab()
            footer_verification.check_url_opened('https://vk.company/ru/company/business/')

    def test_change_language(self, main_page, footer_verification):
        with allure.step("Меняем язык на английский и проверяем выбор языка в футере"):
            main_page.change_language('English')
            footer_verification.check_selected_language('EN')

        with allure.step("Меняем язык на русский и проверяем выбор языка в футере"):
            main_page.change_language('Русский')
            footer_verification.check_selected_language('RU')

    @pytest.mark.parametrize("social_media_url", [
        'https://vk.com/vk_ads',
        'https://ok.ru/group/64279825940712',
        'https://t.me/vk_ads'
    ])
    def test_go_to_social_media(self, main_page, social_media_url, footer_verification):
        with allure.step(
                f"Нажимаем на ссылку в соцсети и проверяем, что открывается нужная страница: {social_media_url}"):
            main_page.click_social_media_item(social_media_url)
            main_page.go_to_new_tab()
            footer_verification.check_url_opened(social_media_url)

    def test_go_to_about(self, main_page, footer_verification):
        with allure.step("Нажимаем на ссылку 'О компании' в футере и проверяем редирект"):
            main_page.click_footer_about()
            main_page.go_to_new_tab()
            footer_verification.check_url_opened('https://vk.company/ru/')

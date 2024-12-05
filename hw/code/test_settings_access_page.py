import allure
from base_case import BaseCase


class TestSettingsAccessPage(BaseCase):
    def test_is_header_and_sign_became_visible(self, settings_access_page, settings_access_page_verification):
        with allure.step("Проверяем видимость заголовка, знака и кнопки добавления"):
            settings_access_page_verification.check_header_and_sign_visibility()

    def test_is_on_more_click_redirected(self, settings_access_page):
        with allure.step("Проверяем редирект по ссылке 'more'"):
            settings_access_page.click_more_link()
            settings_access_page.go_to_new_tab()
            assert self.is_opened('https://ads.vk.com/help/articles/additionalaccounts')

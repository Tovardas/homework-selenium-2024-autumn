from base_case import BaseCase
import allure


class TestForumPage(BaseCase):
    def test_title_is_displayed(self, forum_page, forum_page_verification):
        with allure.step("Проверяем, что заголовок страницы соответствует 'Форум идей'"):
            forum_page_verification.check_page_title('Форум идей')

    def test_go_to_page_of_event(self, forum_page, forum_page_verification):
        with allure.step("Переходим на страницу события и проверяем редирект"):
            forum_page.click_event_item()
            forum_page_verification.check_url_opened('https://ads.vk.com/upvote/19')
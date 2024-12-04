import allure
from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = "Tester Audience"
SOURCE_NAME = "Ключевые фразы"
KEY_PHRASES = ["business", "tasks"]


class TestAudiencePage(BaseCase):
    @allure.title("Открытие модального окна создания аудитории")
    def test_create_audience_modal_page_opened(self, audience_page, verification):
        with allure.step("Нажать на кнопку 'Создать аудиторию' и проверить элементы окна"):
            audience_page.click_create_audience_button()
            verification.check_create_audience_modal_elements()

    @allure.title("Закрытие модального окна создания аудитории")
    def test_create_audience_modal_page_closed(self, audience_page, verification):
        with allure.step("Закрыть окно через крестик"):
            audience_page.click_create_audience_button()
            audience_page.click_cross_button()
            verification.check_create_audience_modal_elements()

        with allure.step("Закрыть окно через кнопку 'Отмена'"):
            audience_page.click_create_audience_button()
            audience_page.click_cancel_button()
            verification.check_create_audience_modal_elements()

    @allure.title("Ошибка при вводе слишком длинного имени аудитории")
    def test_error_long_audience_name(self, audience_page, verification):
        with allure.step("Ввести слишком длинное имя аудитории"):
            audience_page.click_create_audience_button()
            audience_page.enter_audience_name('мяу' * 255)
            verification.check_error_message(audience_page.ERROR_TOO_LONG_AUDIENCE_NAME)

    @allure.title("Открытие модального окна для добавления источника")
    def test_add_source_modal_page_became_visible(self, audience_page, verification):
        with allure.step("Открыть окно добавления источника"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            verification.check_add_source_modal_elements()

    @allure.title("Создание и удаление аудитории")
    def test_create_and_delete_audience(self, audience_page, verification):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME)
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            verification.check_audience_created(CUSTOM_AUDIENCE_NAME)

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            verification.check_audience_deleted()

    @allure.title("Поиск созданной аудитории")
    def test_try_to_find_audience_success(self, audience_page, verification):
        with allure.step("Создание аудитории"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME)
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()

        with allure.step("Поиск по имени аудитории"):
            audience_page.seach_audience_by_name(CUSTOM_AUDIENCE_NAME)
            verification.check_audience_item_visible()

        with allure.step("Удаление аудитории"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            verification.check_audience_deleted()

    @allure.title("Ошибка при поиске аудитории")
    def test_try_to_find_audience_error(self, audience_page, verification):
        with allure.step("Создание аудитории"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME)
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()

        with allure.step("Поиск по несуществующему имени"):
            audience_page.seach_audience_by_name('ERROR')
            verification.check_audience_item_invisible()

        with allure.step("Повторный поиск по реальному имени"):
            audience_page.seach_audience_by_name(CUSTOM_AUDIENCE_NAME)
            verification.check_audience_item_visible()

        with allure.step("Удаление аудитории"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            verification.check_audience_deleted()

import allure

from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = "Tester Audience"
SOURCE_NAME = ["Ключевые фразы", "Подписчики сообществ", "Существующая аудитория"]
KEY_PHRASES = ["учеба", "обучение"]
MINUS_PHRASES = ["лень", "бездельник"]
GROUPS = ["VK Education", "МГТУ им. Н.Э. Баумана"]
GROUPS2 = ["Reddit"]


class TestAudiencePage(BaseCase):
    @allure.title("Ошибка при вводе слишком длинного имени аудитории")
    def test_error_long_audience_name(self, audience_page):
        with allure.step("Ввести слишком длинное имя аудитории"):
            audience_page.click_create_audience_button()
            audience_page.enter_audience_name('мяу' * 255)
            assert self.audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    @allure.title("Создание и удаление аудитории")
    def test_create_and_delete_audience(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience2(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.enter_minus_phrases(MINUS_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience3(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[1])
            audience_page.enter_groups(GROUPS)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience4(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[1])
            audience_page.enter_groups(GROUPS)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[2])
            audience_page.choose_existingsources()
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience5(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[1])
            audience_page.enter_groups(GROUPS)
            audience_page.click_modal_page_submit_button()
            audience_page.change_option('хотя бы одному из условий')
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME


            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[2])
            audience_page.choose_existingsources()
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience6(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[1])
            audience_page.enter_groups(GROUPS)
            audience_page.click_modal_page_submit_button()
            audience_page.change_option('ни одному из условий')
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME


            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[2])
            audience_page.choose_existingsources()
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_edit_audience(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[0])
            audience_page.enter_key_phrases(KEY_PHRASES)
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Редактировать аудиторию"):
            audience_page.edit_audience('хотя бы одному из условий')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.edit_audience('ни одному из условий')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.edit_audience('всем условиям')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.edit_audience('ни одному из условий')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.edit_audience('хотя бы одному из условий')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

            audience_page.edit_audience('всем условиям')
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()




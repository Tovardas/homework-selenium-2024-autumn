import allure

from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = "Tester Audience"
SOURCE_NAME = ["Ключевые фразы", "Подписчики сообществ", "Существующая аудитория", "Список пользователей", "События в лид-форме", "события на сайте"]
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

    def test_create_and_delete_audience7(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[3])
            audience_page.upload_id_file()
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience8(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[3])
            audience_page.select_existing_file()
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_leadfrom(self, leadforms_page):
        with allure.step("Создаем лид-форму"):
            leadforms_page.click_create_leadform_button()
            leadforms_page.click_last_image_name_from_media_library()

            leadforms_page.fill_1_compact_all_data('Наша лид форма', 'Техносад', 'Наша лид форма', 'Обязательно к прохождению')
            leadforms_page.continue_1()
            leadforms_page.continue_1()

            leadforms_page.fill_3_header('Спасибо, до свидания')
            leadforms_page.fill_3_description('Кредит одобрен')
            leadforms_page.continue_1()

            leadforms_page.fill_4_name('Аркадий Паровозов')
            leadforms_page.fill_4_address('г. Саратов, ул. Вторая, д.14 кв. 99')

            assert leadforms_page.get_form_name() == 'Наша лид форма'

    def test_create_and_delete_audience9(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Открытие формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience10(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Открытие формы')
            audience_page.click_checkbox('Отправка формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience11(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Отправка формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience12(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Открытие формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience13(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Открытие формы')
            audience_page.click_checkbox('Отправка формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience14(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[4])
            audience_page.set_existing_lead_form()
            audience_page.click_checkbox('Отправка формы')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_delete_leadfrom(self, leadforms_page):
        with allure.step("Удаляем лид-форму"):
            leadforms_page.remove_lead_form()

    def test_create_and_delete_audience15(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('Посещение сайта')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience16(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('Посещение сайта')
            audience_page.click_checkbox('testing event')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience17(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('testing event')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()


    def test_create_and_delete_audience18(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('Посещение сайта')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience19(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('Посещение сайта')
            audience_page.click_checkbox('testing event')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience20(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_checkbox('testing event')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience21(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('ВК')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience22(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('Обучение')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience23(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_add_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('ВК')
            audience_page.click_checkbox('Обучение')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience24(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('ВК')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience25(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('Обучение')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        with allure.step("Удалить аудиторию"):
            audience_page.hover_and_click_delete()
            audience_page.click_delete_confirm_button()
            assert self.audience_page.audience_item_became_invisible()

    def test_create_and_delete_audience26(self, audience_page):
        with allure.step("Создать аудиторию"):
            audience_page.click_create_audience_button()
            audience_page.click_discard_source_button()
            audience_page.select_source(SOURCE_NAME[5])
            audience_page.select_first_pixel()
            audience_page.click_audition_tags_button()
            audience_page.click_checkbox('ВК')
            audience_page.click_checkbox('Обучение')
            audience_page.click_modal_page_submit_button()
            audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
            audience_page.click_modal_page_submit_button()
            assert self.audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

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




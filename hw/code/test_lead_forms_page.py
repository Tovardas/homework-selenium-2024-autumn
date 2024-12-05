import os

from base_case import BaseCase

LEADFORM_NAME = 'Запись на тестовый урок'
FILEPATH = os.path.join(os.path.dirname(__file__), 'images/nya.png')
COMPANY_NAME = 'Easy English'
LEADFORM_TITLE = 'Проверь свой уровень английского'
LEADFORM_DESCRIPTION = 'Мы пришлем результат на почту'
GRADIENT_NUMBER = 5

QUESTIONS_AND_ANSWERS = {
    'Как переводится с английского слово Strawberry?': ['Клубника', 'Ежевика', 'Малина', 'Голубика'],
    'Как переводится с английского слово Bird?': ['птица', 'петь']
}

ADDITIONAL_CONTACT_INFO_TYPES = ['Электронная почта', 'Фамилия']

RESULT_TITLE = 'Тест пройден!'
RESULT_DESCRIPTION = 'В течение 15 минут вам на почту придет результат'
COMPANY_URL = 'https://easyenglish.best/'
COMPANY_PHONE = '+79999999999'

NOTIFICATIONS_EMAIL = 'notifications@easyenglish.ru'
FULL_NAME = 'Петров Петр'
ADDRESS = 'г.Москва, ул.Никитина, д.1, кв.600'
EMAIL = 'petrov@easyenglish.ru'
INN = '3663065397'


class TestLeadFormsPage(BaseCase):
    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)
        assert leadforms_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)

        leadforms_page.delete_all_from_media_library()

    def test_1_compact_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.empty_1_compact_all_data()
        leadforms_page.continue_1()
        leadforms_page.check_empty_1_compact_all('Обязательное поле')

    def test_1_compact_max_length(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_1_compact_all_data('a' * 256, 'a' * 31, 'a' * 51, 'a' * 36)
        leadforms_page.continue_1()
        leadforms_page.check_errors_1_compact_all('Превышена максимальная длина поля')

    def test_1_more_text_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_more_text()
        leadforms_page.empty_1_more_text_data()
        leadforms_page.continue_1()
        leadforms_page.check_empty_1_more_text('Обязательное поле')

    def test_1_more_text_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_more_text()
        leadforms_page.fill_1_more_text_data('a' * 351)
        leadforms_page.continue_1()
        leadforms_page.check_empty_1_more_text('Превышена максимальная длина поля')

    def test_1_magnet_bonus_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_bonus()

        leadforms_page.empty_1_magnet_bonus()
        leadforms_page.continue_1()
        leadforms_page.check_empty_1_magnet_bonus('Обязательное поле')

        leadforms_page.fill_1_magnet_bonus('a' * 31)
        leadforms_page.continue_1()
        leadforms_page.check_error_1_magnet_bonus('Превышена максимальная длина поля')

    def test_1_magnet_sale_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.click_1_magnet()
        leadforms_page.click_1_magnet_sale()

        leadforms_page.fill_1_magnet_sale(0)
        leadforms_page.continue_1()
        leadforms_page.check_zero_1_magnet_sale('Значение должно быть больше нуля')

        leadforms_page.click_1_magnet_sale_percent()
        leadforms_page.fill_1_magnet_sale(101)
        leadforms_page.continue_1()
        leadforms_page.check_over_1_magnet_sale('Укажите скидку не больше 100%')

    def test_2_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.continue_1()

        leadforms_page.create_question_2()
        leadforms_page.continue_1()
        leadforms_page.check_question_2_error('Вопрос должен быть не пустым и содержать минимум 2 ответа')

        leadforms_page.fill_2_question('a' * 3)
        leadforms_page.continue_1()
        leadforms_page.check_question_2_error('Вопрос должен быть не пустым и содержать минимум 2 ответа')

        leadforms_page.fill_2_answer_1('a' * 3)
        leadforms_page.continue_1()
        leadforms_page.check_question_2_error('Вопрос должен быть не пустым и содержать минимум 2 ответа')

    def test_2_contacts_error(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.continue_1()

        leadforms_page.click_2_bin_name()
        leadforms_page.click_2_bin_phone()
        leadforms_page.check_error_2_contacts('Минимальное количество полей: 1')

    def test_3_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.empty_3_header()
        leadforms_page.continue_1()
        leadforms_page.check_empty_3_heading('Обязательное поле')

        leadforms_page.fill_3_header('a' * 26)
        leadforms_page.fill_3_description('a' * 161)
        leadforms_page.continue_1()
        leadforms_page.check_errors_3_heading('Превышена максимальная длина поля')

    def test_3_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.click_3_site()
        leadforms_page.click_3_phone()
        leadforms_page.click_3_promocode()

        leadforms_page.fill_3_site('a')
        leadforms_page.fill_3_phone('a')
        leadforms_page.fill_3_promocode('a' * 31)
        leadforms_page.continue_1()
        leadforms_page.check_errors_3_site('Невалидный url')
        leadforms_page.check_errors_3_phone('Телефон должен начинаться с + и содержать только цифры')
        leadforms_page.check_errors_3_promocode('Превышена максимальная длина поля')

    def test_4(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form_1()
        leadforms_page.upload_image(FILEPATH)
        leadforms_page.continue_1()
        leadforms_page.continue_1()
        leadforms_page.continue_1()

        leadforms_page.empty_4_name()
        leadforms_page.empty_4_address()
        leadforms_page.continue_1()
        leadforms_page.check_4_errors_empty('Обязательное поле')

        leadforms_page.fill_4_name('a' * 256)
        leadforms_page.fill_4_address('a' * 256)
        leadforms_page.fill_4_inn('a' * 33)
        leadforms_page.continue_1()
        leadforms_page.check_4_errors_empty('Превышена максимальная длина поля')

        leadforms_page.fill_4_email('a')
        leadforms_page.check_4_error_email('Некорректный email адрес')

        leadforms_page.click_4_notify()
        leadforms_page.fill_4_notify_email('a')
        leadforms_page.continue_1()
        leadforms_page.check_4_error_notify_email('Поле содержит невалидный email адрес')

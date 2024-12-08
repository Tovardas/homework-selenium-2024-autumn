import allure

from base_case import BaseCase


class TestSettingsCommonPage(BaseCase):
    FULL_NAME = 'Tester T T'
    INN = '123456789012'
    VALID_INN = ['312947019840', '756709877700', '482081431745']
    VALID_NAME = ['Иван Иванов Иванович', 'иван иванов иванович', 'Иван', 'иван', 'Иванов', 'Иванович', 'сунь-зы', 'сунь - Зы', 'Иван-', '-Иван', '-Иван-', 'ы', 'и в а', '-и-в-а-']

    def test_base_details_change(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[0])
            settings_common_page.enter_inn(self.VALID_INN[0])

    def test_is_error_invalid_phone_number(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку при вводе некорректного номера телефона"):
            settings_common_page.enter_phone_number('7985285313')
            settings_common_page_verification.check_phone_number_error()

    def test_is_additional_email_inputs_became_visible(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем, что дополнительные поля для ввода email становятся видимыми"):
            settings_common_page_verification.check_additional_email_inputs_visibility()

    def test_is_error_invalid_email(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку при вводе некорректного email"):
            settings_common_page.click_add_email_button()
            settings_common_page.enter_email('invalid')
            settings_common_page_verification.check_email_error()

    def test_is_error_empty_fields(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку для пустых полей"):
            settings_common_page.click_add_email_button()
            settings_common_page.enter_email('')
            settings_common_page_verification.check_empty_field_errors()

    def test_is_error_too_short_inn(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку для слишком короткого ИНН"):
            settings_common_page.enter_inn('123456')
            settings_common_page_verification.check_inn_error('too_short')

    def test_is_error_invalid_inn(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку для некорректного ИНН"):
            settings_common_page.enter_inn('11111111111a')
            settings_common_page_verification.check_inn_error('invalid')

    def test_logout_other_devices(self, settings_common_page):
        with allure.step("Проверяем выход из аккаунта на других устройствах"):
            settings_common_page.click_logout_other_devices_button()
            assert settings_common_page.logout_devices_success_message_became_visible()

    def test_is_delete_cabinet_modal_page_became_visible(self, settings_common_page):
        with allure.step("Проверяем, что появляется модальное окно для удаления кабинета"):
            settings_common_page.click_delete_cabinet_button()
            assert settings_common_page.delete_cabinet_modal_page_became_visible()

    def test_cancel_changes(self, settings_common_page):
        with allure.step("Проверяем отмену изменений в поле 'ФИО'"):
            full_name_before = settings_common_page.get_full_name_field_value()
            settings_common_page.enter_full_name(self.FULL_NAME)
            settings_common_page.click_cancel_button()
            assert settings_common_page.get_full_name_field_value() == full_name_before

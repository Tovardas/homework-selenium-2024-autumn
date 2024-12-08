import allure

from base_case import BaseCase


class TestSettingsCommonPage(BaseCase):
    VALID_INN = ['312947019840', '756709877700', '482081431745']
    VALID_NAME = ['Иван Иванов Иванович', 'иван иванов иванович', 'Иван', 'иван', 'Иванов', 'Иванович', 'сунь-зы', 'сунь - Зы', 'Иван-', '-Иван', '-Иван-', 'ы', 'и в а', '-и-в-а-']
    VALID_PHONE = ['+7915111111133', '+791511111113', '+79151111111', '+8915111111113', '+891511111113', '+89151111111']
    VALID_EMAIL = ['alex_gorbatov_test01_003@mail.ru', 'alex_gorbatov_test01_003@alexgorbatovtest01003.ru', 'alex_gorbatov_test01_003@alexgorbatovtest01003.alexgorbatovtest', 'a@alexgorbatovtest.alexgorbatovtest', 'a@a.aa', '756709877700@a.aa', 'alex_gorbatov_test01_003@mail.ruтест', 'alex_gorbatov_test01_003@mailтест.ruтест', 'alex_gorbatov_test01_003@mail.тест.ru.тест', 'alex_gorbatov_test01_003@mail.тест.ru.т.е.ст']

    def test_base_details_change_0_2(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[0])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[0])
            settings_common_page.enter_inn(self.VALID_INN[2])
            assert settings_common_page.is_inn_matches(self.VALID_INN[2])

    def test_base_details_change_1_1(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[1])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[1])
            settings_common_page.enter_inn(self.VALID_INN[1])
            assert settings_common_page.is_inn_matches(self.VALID_INN[1])

    def test_base_details_change_2_0(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[2])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[2])
            settings_common_page.enter_inn(self.VALID_INN[0])
            assert settings_common_page.is_inn_matches(self.VALID_INN[0])

    def test_base_details_change_3_0(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[3])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[3])
            settings_common_page.enter_inn(self.VALID_INN[0])
            assert settings_common_page.is_inn_matches(self.VALID_INN[0])

    def test_base_details_change_4_1(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[4])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[4])
            settings_common_page.enter_inn(self.VALID_INN[1])
            assert settings_common_page.is_inn_matches(self.VALID_INN[1])

    def test_base_details_change_5_2(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[5])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[5])
            settings_common_page.enter_inn(self.VALID_INN[2])
            assert settings_common_page.is_inn_matches(self.VALID_INN[2])

    def test_base_details_change_6_2(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[6])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[6])
            settings_common_page.enter_inn(self.VALID_INN[2])
            assert settings_common_page.is_inn_matches(self.VALID_INN[2])

    def test_base_details_change_7_1(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[7])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[7])
            settings_common_page.enter_inn(self.VALID_INN[1])
            assert settings_common_page.is_inn_matches(self.VALID_INN[1])

    def test_base_details_change_8_0(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[8])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[8])
            settings_common_page.enter_inn(self.VALID_INN[0])
            assert settings_common_page.is_inn_matches(self.VALID_INN[0])

    def test_base_details_change_9_2(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[9])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[9])
            settings_common_page.enter_inn(self.VALID_INN[2])
            assert settings_common_page.is_inn_matches(self.VALID_INN[2])

    def test_base_details_change_10_0(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[10])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[10])
            settings_common_page.enter_inn(self.VALID_INN[0])
            assert settings_common_page.is_inn_matches(self.VALID_INN[0])

    def test_base_details_change_11_1(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[11])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[11])
            settings_common_page.enter_inn(self.VALID_INN[1])
            assert settings_common_page.is_inn_matches(self.VALID_INN[1])

    def test_base_details_change_12_0(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[12])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[12])
            settings_common_page.enter_inn(self.VALID_INN[0])
            assert settings_common_page.is_inn_matches(self.VALID_INN[0])

    def test_base_details_change_13_2(self, settings_common_page):
        with allure.step("Проверка изменения реквизитов на базовые параметры"):
            settings_common_page.enter_full_name(self.VALID_NAME[13])
            assert settings_common_page.is_full_name_matches(self.VALID_NAME[13])
            settings_common_page.enter_inn(self.VALID_INN[2])
            assert settings_common_page.is_inn_matches(self.VALID_INN[2])


    def test_base_email_change_start(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.click_add_email_button()
            settings_common_page.enter_email(self.VALID_EMAIL[0])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[0])

    def test_base_email_change_resume(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[1])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[1])

    def test_base_email_change_resume1(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[1])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[1])

    def test_base_email_change_resume2(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[2])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[2])

    def test_base_email_change_resume3(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[3])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[3])

    def test_base_email_change_resume4(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[4])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[4])

    def test_base_email_change_resume5(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[5])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[5])

    def test_base_email_change_resume6(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[6])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[6])

    def test_base_email_change_resume7(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[7])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[7])

    def test_base_email_change_resume8(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[8])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[8])

    def test_base_email_change_resume9(self, settings_common_page):
        with allure.step("Проверка изменения почты"):
            settings_common_page.enter_email(self.VALID_EMAIL[9])
            assert settings_common_page.is_email_matches(self.VALID_EMAIL[9])


    def test_base_phone_change_0(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[0])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[0])

    def test_base_phone_change_1(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[1])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[1])

    def test_base_phone_change_2(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[2])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[2])

    def test_base_phone_change_3(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[3])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[3])

    def test_base_phone_change_4(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[4])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[4])

    def test_base_phone_change_5(self, settings_common_page):
        with allure.step("Проверка изменения телефона"):
            settings_common_page.enter_phone_number(self.VALID_PHONE[5])
            assert settings_common_page.is_phone_matches(self.VALID_PHONE[5])

    def test_is_error_invalid_phone_number(self, settings_common_page, settings_common_page_verification):
        with allure.step("Проверяем ошибку при вводе некорректного номера телефона"):
            settings_common_page.enter_phone_number('7985285313')
            settings_common_page_verification.check_phone_number_error()

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
            settings_common_page.enter_full_name(self.VALID_NAME[0])
            settings_common_page.click_cancel_button()
            assert settings_common_page.get_full_name_field_value() == full_name_before

from base_case import BaseCase
import allure

class TestBudgetPage(BaseCase):

    @allure.title("Открытие модального окна пополнения бюджета")
    def test_is_opened_replenishment_modal_page(self, budget_page, budget_page_verification):
        with allure.step("Открываем модальное окно пополнения бюджета и проверяем его отображение"):
            budget_page.click_replenish_budget_button()
            budget_page_verification.check_replenishment_modal_opened()

    @allure.title("Закрытие модального окна пополнения бюджета")
    def test_is_closed_replenishment_modal_page(self, budget_page, budget_page_verification):
        with allure.step("Закрываем модальное окно пополнения бюджета и проверяем его скрытие"):
            budget_page.click_replenish_budget_button()
            budget_page.close_replenishment_modal_page()
            budget_page_verification.check_replenishment_modal_closed()

    @allure.title("Ошибка при указании слишком маленькой суммы пополнения")
    def test_is_error_too_little_amount(self, budget_page, budget_page_verification):
        with allure.step("Вводим слишком маленькую сумму и проверяем сообщение об ошибке"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount(budget_page.MIN_AMOUNT - 1)
            budget_page.click_submit_button()
            budget_page_verification.check_error_message(budget_page.ERROR_TOO_LITTLE_AMOUNT)

    @allure.title("Ошибка при указании слишком маленькой суммы без учета НДС")
    def test_is_error_too_little_amount_without_vat(self, budget_page, budget_page_verification):
        with allure.step("Вводим слишком маленькую сумму без НДС и проверяем сообщение об ошибке"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount_without_vat(budget_page.MIN_AMOUNT_WITHOUT_VAT - 1)
            budget_page.click_submit_button()
            budget_page_verification.check_error_message(budget_page.ERROR_TOO_LITTLE_AMOUNT)

    @allure.title("Ошибка при указании слишком большой суммы пополнения")
    def test_is_error_too_large_amount(self, budget_page, budget_page_verification):
        with allure.step("Вводим слишком большую сумму и проверяем сообщение об ошибке"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount(budget_page.MAX_AMOUNT + 1)
            budget_page.click_submit_button()
            budget_page_verification.check_error_message(budget_page.ERROR_TOO_LARGE_AMOUNT)

    @allure.title("Ошибка при указании слишком большой суммы без учета НДС")
    def test_is_error_too_large_amount_without_vat(self, budget_page, budget_page_verification):
        with allure.step("Вводим слишком большую сумму без НДС и проверяем сообщение об ошибке"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount_without_vat(budget_page.MAX_AMOUNT_WITHOUT_VAT + 1)
            budget_page.click_submit_button()
            budget_page_verification.check_error_message(budget_page.ERROR_TOO_LARGE_AMOUNT)

    @allure.title("Ввод нечислового значения в поле суммы")
    def test_enter_non_numeric_amount(self, budget_page, budget_page_verification):
        with allure.step("Вводим нечисловое значение в поле суммы и проверяем, что оно очищается"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount('letters $#!!#*&(!)!_')
            budget_page_verification.check_amount_field_empty()

    @allure.title("Ввод нечислового значения в поле суммы без учета НДС")
    def test_enter_non_numeric_amount_without_vat(self, budget_page, budget_page_verification):
        with allure.step("Вводим нечисловое значение в поле суммы без НДС и проверяем, что оно очищается"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount_without_vat('SLOVNO... !@#$%^&')
            budget_page_verification.check_amount_without_vat_field_empty()

    @allure.title("Проверка вычета НДС")
    def test_vat_deduction(self, budget_page, budget_page_verification):
        with allure.step("Вводим сумму с НДС и проверяем корректность вычета НДС"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount(600)
            budget_page_verification.check_vat_deduction('500 ₽')

    @allure.title("Проверка добавления НДС")
    def test_vat_addition(self, budget_page, budget_page_verification):
        with allure.step("Вводим сумму без НДС и проверяем корректность добавления НДС"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount_without_vat(800)
            budget_page_verification.check_vat_addition('960 ₽')

    @allure.title("Открытие VKPay iframe")
    def test_is_open_vkpay_iframe(self, budget_page, budget_page_verification):
        with allure.step("Вводим минимальную сумму, подтверждаем и проверяем отображение iframe VKPay"):
            budget_page.click_replenish_budget_button()
            budget_page.enter_amount(budget_page.MIN_AMOUNT)
            budget_page.click_submit_button()
            budget_page_verification.check_vkpay_iframe_visible()

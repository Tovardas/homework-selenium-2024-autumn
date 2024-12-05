import allure

from base_case import BaseCase


class TestSettingsNotificationsPage(BaseCase):
    def test_h2_became_visible(self, settings_notifications_page, settings_notifications_page_verification):
        with allure.step("Проверяем видимость заголовка h2 и других элементов на странице настроек уведомлений"):
            settings_notifications_page_verification.check_elements_visibility()

    def test_is_on_cancel_click_checkbox_returned(self, settings_notifications_page,
                                                  settings_notifications_page_verification):
        with allure.step("Проверяем, что при нажатии 'Отмена' состояние чекбокса сохраняется"):
            checked = settings_notifications_page.checkbox_checked()
            settings_notifications_page.click_checkbox()
            settings_notifications_page.click_cancel()
            settings_notifications_page_verification.check_checkbox_state(checked)

    def test_is_on_save_click_checkbox_saved(self, settings_notifications_page,
                                             settings_notifications_page_verification):
        with allure.step("Проверяем, что при нажатии 'Сохранить' состояние чекбокса сохраняется"):
            checked = settings_notifications_page.checkbox_checked()
            settings_notifications_page.click_checkbox()
            settings_notifications_page.click_save()
            settings_notifications_page_verification.check_checkbox_state(not checked)

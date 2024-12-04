from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.settings_notifications_page_locators import SettingsNotificationsPageLocators


class SettingsNotificationsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/notifications'
    locators = SettingsNotificationsPageLocators()

    H2_LIST = ['Способы получения', 'Основные', 'Новости и акции']
    CHECKBOX_LIST = ['Финансы', 'Модерация', 'Рекламные кампании', 'Правила для объявлений', 'Изменения в API', 'Новости', 'Мероприятия', 'Акции, спецпредложения и прочие']

    def h2_became_visible(self):
        for h in self.H2_LIST:
            if not self.became_visible(self.locators.H2_NAME(h)):
                return False
        return True

    def checkbox_became_visible(self):
        for h in self.CHECKBOX_LIST:
            if not self.became_visible(self.locators.CHECKBOX_NAME(h)):
                return False
        return True

    def switch_email_became_visible(self):
        return self.became_visible(self.locators.SWITCH_EMAIL_SIGN) and self.became_visible(self.locators.SWITCH_EMAIL_INPUT)
    
    def telegram_became_visible(self):
        return self.became_visible(self.locators.TELEGRAM_SIGN) and self.became_visible(self.locators.TELEGRAM_BUTTON)

    def save_modal_became_visible(self):
        return self.became_visible(self.locators.SAVE_MODAL) and self.became_visible(self.locators.SAVE_MODAL_CANCEL) and self.became_visible(self.locators.SAVE_MODAL_SAVE)
    
    def click_switch(self):
        return self.click(self.locators.SWITCH_EMAIL_INPUT)
    
    def click_checkbox(self):
        return self.click(self.locators.CHECKBOX_NAME(self.CHECKBOX_LIST[2]))
    
    def click_cancel(self):
        return self.click(self.locators.SAVE_MODAL_CANCEL)
    
    def click_save(self):
        return self.click(self.locators.SAVE_MODAL_SAVE)
    
    def checkbox_not_checked(self):
        return self.became_visible(self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT(self.CHECKBOX_LIST[2], 'off'))
    
    def checkbox_checked(self):
        return self.became_visible(self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT(self.CHECKBOX_LIST[2], 'on'))    
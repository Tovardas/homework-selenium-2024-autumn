from ui.locators.cabinet_page_locators import CabinetPageLocators
from ui.pages.base_page import BasePage


class CabinetPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = CabinetPageLocators()

    def click_left_menu(self, item_name):
        self.click(self.locators.LEFT_MENU_ITEM(item_name))

    def click_balance_button(self):
        self.click(self.locators.BALANCE_BUTTON)

    def click_notifications_button(self):
        self.click(self.locators.NOTIFICATIONS_BUTTON)

    def notifications_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.NOTIFICATIONS_MODAL_PAGE)

    def click_user_avatar(self):
        self.click(self.locators.USER_AVATAR)

    def user_menu_became_visible(self) -> bool:
        return self.became_visible(self.locators.USER_MENU)

    def click_logout_button(self):
        self.click(self.locators.LOGOUT_BUTTON)

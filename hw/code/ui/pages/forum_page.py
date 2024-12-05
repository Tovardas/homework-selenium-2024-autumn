from ui.locators.forum_page_locators import ForumsPageLocators
from ui.pages.base_page import BasePage


class ForumsPage(BasePage):
    locators = ForumsPageLocators()
    url = 'https://ads.vk.com/upvote'

    def click_event_item(self):
        self.click(self.locators.FORUM_BLOCK)

    def get_page_title(self):
        return self.find(self.locators.SUMMARY_TITLE_ADS).text

from ui.locators.guide_no_reg_page_locators import GuideNoRegPageLocators
from ui.pages.base_page import BasePage


class GuideNoRegPage(BasePage):
    locators = GuideNoRegPageLocators()

    def click_materials_button(self):
        self.hover(self.locators.GUIDE_NAME)
        self.click(self.locators.GUIDE_MATERIALS_NAME)

    def click_events_button(self):
        self.hover(self.locators.GUIDE_NAME)
        self.click(self.locators.GUIDE_EVENTS_NAME)

    def click_videos_button(self):
        self.hover(self.locators.GUIDE_NAME)
        self.click(self.locators.GUIDE_VIDEOS_NAME)

    def click_certification_button(self):
        self.hover(self.locators.GUIDE_NAME)
        self.click(self.locators.GUIDE_CERTIFICATION_NAME)

    def click_materials_card(self):
        self.click(self.locators.MATERIALS_CARD)

    def click_materials_tag(self):
        self.click(self.locators.MATERIALS_TAG)

    def click_materials_content(self):
        self.scroll_and_click(self.locators.MATERIALS_CONTENT_LINK)

    def header_became_visible(self) -> bool:
        return self.became_visible(self.locators.MATERIALS_CONTENT_HEADER)

    def click_materials_cabinet_button(self):
        self.scroll_and_click(self.locators.MATERIALS_CABINET_NAME)

    def click_pagination_number(self):
        self.scroll_and_click(self.locators.MATERIALS_PAGINATION_NUMBER)

    def click_pagination_left(self):
        self.scroll_and_click(self.locators.MATERIALS_PAGINATION_LEFT)

    def click_pagination_right(self):
        self.scroll_and_click(self.locators.MATERIALS_PAGINATION_RIGHT)

    def click_events_card_old(self):
        self.scroll_and_click(self.locators.EVENTS_CARD_OLD)

    def event_contains_video(self) -> bool:
        self.scroll_and_click(self.locators.EVENTS_VIDEO)
        return self.became_visible(self.locators.EVENTS_VIDEO)

    def click_events_card_new(self):
        self.scroll_and_click(self.locators.EVENTS_CARD_NEW)

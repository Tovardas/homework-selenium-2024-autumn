from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.guide_page_locators import GuidePageLocators
from ui.pages.base_page import BasePage


class GuidePage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = GuidePageLocators()

    def is_element_displayed(self, locator):
        try:
            self.wait().until(EC.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False

    def click_guide_button(self):
        self.hover(self.locators.HELP_AND_GUIDE)
        self.click(self.locators.GUIDE_BUTTON)

    def modal_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.GUIDE_MODAL)

    def click_guide_close_button(self):
        self.click(self.locators.GUIDE_CLOSE_BUTTON)

    def inner_modal_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.INNER_MODAL)

    def click_group_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_pixel_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_catalog_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_mobile_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_lidforms_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_miniapps_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_music_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_video_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_dzen_modal_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)

    def click_video_button(self):
        self.click(self.locators.PIXEL_VIDEO_BUTTON)

    def click_platform_button(self):
        self.click(self.locators.PIXEL_PLATFORM_BUTTON)

    def video_is_displayed(self) -> bool:
        return self.is_element_displayed(self.locators.PIXEL_VIDEO_ELEMENT)

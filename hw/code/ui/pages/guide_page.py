from ui.pages.base_page import BasePage
from ui.locators.guide_page_locators import GuidePageLocators

class GuidePage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = GuidePageLocators()

    def guide_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.GUIDE_MODAL)
    
    def guide_inner_modal_became_visible(self) -> bool:
        return self.became_visible(self.locators.INNER_MODAL)
    
    def guide_campaign_button_became_visible(self) -> bool:
        return self.became_visible(self.locators.CAMPAIGN_MODAL_BUTTON)
    
    def guide_campaign_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CAMPAIGN_BUTTON)
    
    def guide_campaign_video_became_visible(self) -> bool:
        return self.became_visible(self.locators.VIDEO_MODAL)

    def click_guide_button(self):
        self.click(self.locators.GUIDE_BUTTON)
        
    def click_guide_close_button(self):
        self.click(self.locators.GUIDE_CLOSE_BUTTON)
        
    def click_guide_community_button(self):
        self.click(self.locators.COMMUNITY_BUTTON)
        
    def click_guide_catalog_button(self):
        self.click(self.locators.CATALOG_BUTTON)

    def click_campaign_modal_button(self):
        self.click(self.locators.CAMPAIGN_MODAL_BUTTON)

    def click_campaign_button(self):
        self.click(self.locators.CAMPAIGN_BUTTON)

    def click_video_button(self):
        self.click(self.locators.VIDEO_BUTTON)
        
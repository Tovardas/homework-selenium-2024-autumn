class GuidePageVerification:
    def __init__(self, guide_page):
        self.guide_page = guide_page

    def check_modal_is_displayed(self):
        assert self.guide_page.modal_is_displayed()

    def check_inner_modal_is_displayed(self):
        assert self.guide_page.inner_modal_is_displayed()

    def check_video_is_displayed(self):
        assert self.guide_page.video_is_displayed()

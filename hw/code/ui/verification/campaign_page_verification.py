class CampaignVerification:
    def __init__(self, campaign_page):
        self.campaign_page = campaign_page

    def check_create_button_flow(self):
        assert self.campaign_page.name_sign_became_visible()
        assert self.campaign_page.has_tabs_title_content()
        assert self.campaign_page.has_target_tabs_content_name_sign()
        assert self.campaign_page.has_target_tabs_content_cells()

    def check_recognition_tabs(self):
        assert self.campaign_page.has_recognition_tabs_content_name_sign()
        assert self.campaign_page.has_recognition_tabs_content_cells()

    def check_site_inputs(self):
        assert self.campaign_page.site_name_input_became_visible()

    def check_campaign_created(self):
        assert self.campaign_page.banner_became_visible()
        assert self.campaign_page.target_select_became_visible()
        assert self.campaign_page.switch_became_visible()
        assert self.campaign_page.strategy_action_select_became_visible()
        assert self.campaign_page.budget_inputs_became_visible()
        assert self.campaign_page.data_inputs_became_visible()
        assert self.campaign_page.create_footer_became_visible()
        assert self.campaign_page.has_create_footer_continue_button_content()


    def check_group_creation_url(self):
        assert self.campaign_page.name_sign_became_visible()

    def check_region_section(self):
        assert self.campaign_page.has_sections_title_content()
        assert self.campaign_page.has_section_region_region_buttons_content()

    def check_interest_subsection_visibility(self):
        assert self.campaign_page.interest_subsection_became_visible()

    def check_interest_subsection_content(self):
        assert self.campaign_page.has_interest_subsection_content()

    def check_demography_section(self):
        assert self.campaign_page.has_age_select_content()
        assert self.campaign_page.has_pegi_select_content()

    def check_device_section(self):
        assert self.campaign_page.has_device_section_content()

    def check_ad_fields(self):
        assert self.campaign_page.name_sign_became_visible()
        assert self.campaign_page.logo_input_became_visible()
        assert self.campaign_page.has_ads_inputs_content()
        assert self.campaign_page.has_ads_textarea_content()
        assert self.campaign_page.mediatec_became_visible()

    def check_media_sidebar_content(self):
        assert self.campaign_page.has_media_sidebar_content()

    def check_preview_image_visibility(self):
        assert self.campaign_page.preview_image_became_visible()

    def check_media_content_and_buttons(self):
        assert self.campaign_page.media_content_list_became_visible()
        assert self.campaign_page.buttons_changed()

    def check_bug_modal_content(self):
        assert self.campaign_page.has_bug_modal_content()

    def check_campaign_page_state(self):
        assert self.campaign_page.has_campaign_page_tabs_content()
        assert self.campaign_page.action_select_became_visible()
        assert self.campaign_page.checkbox_all_became_visible()
        assert self.campaign_page.check_campaign_title()
        assert self.campaign_page.check_campaign_budget()
        assert self.campaign_page.check_campaign_action()

    def check_edit_button_visibility(self):
        assert self.campaign_page.edit_became_visible()

    def check_campaign_form_values(self):
        assert self.campaign_page.check_title_input_value_campaign()
        assert self.campaign_page.check_site_name_value_campaign()
        assert self.campaign_page.check_action_select_value_campaign()
        assert self.campaign_page.check_strategy_select_value_campaign()
        assert self.campaign_page.check_budget_input_value_campaign()
        assert self.campaign_page.check_budget_period_input_value_campaign()

    def check_group_state_after_cancel(self):
        assert self.campaign_page.check_group_title()
        assert self.campaign_page.action_select_became_visible()
        assert self.campaign_page.checkbox_all_became_visible()

    def check_group_edit_button_visibility(self):
        assert self.campaign_page.edit_became_visible()

    def check_group_form_values(self):
        assert self.campaign_page.check_title_input_value_group()
        assert self.campaign_page.check_selected_region()
        assert self.campaign_page.check_ages()
        assert self.campaign_page.check_pegi()
        assert self.campaign_page.check_interest()
        assert self.campaign_page.check_stop_interest()
        assert self.campaign_page.check_devices()

    def check_ad_state_after_cancel(self):
        assert self.campaign_page.check_ad_title()
        assert self.campaign_page.action_select_became_visible()
        assert self.campaign_page.checkbox_all_became_visible()

    def check_ad_edit_button_visibility(self):
        assert self.campaign_page.edit_became_visible()

    def check_ad_edit_form_values(self):
        assert self.campaign_page.preview_image_became_visible()
        assert self.campaign_page.media_content_list_became_visible()
        assert self.campaign_page.check_ad_name()
        assert self.campaign_page.check_ad_short_description()
        assert self.campaign_page.check_ad_long_description()
        assert self.campaign_page.check_ad_button_text()
        assert self.campaign_page.check_ad_advertiser()
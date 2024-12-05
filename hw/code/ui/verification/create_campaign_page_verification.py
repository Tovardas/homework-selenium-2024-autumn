class CreateCampaignPageVerification:
    def __init__(self, create_campaign_page):
        self.create_campaign_page = create_campaign_page

    def check_url(self, current_url, expected_url):
        assert current_url == expected_url

    def check_advertised_site_field_present(self):
        assert self.create_campaign_page.is_advertised_site_field_present()

    def check_fields_displayed(self):
        assert self.create_campaign_page.fields_displayed()

    def check_url_startswith(self, current_url, expected_url):
        assert current_url.startswith(expected_url)

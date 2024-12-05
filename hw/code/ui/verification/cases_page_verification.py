class CasesPageVerification:
    def __init__(self, cases_page):
        self.cases_page = cases_page

    def check_url_opened(self, current_url, expected_url):
        assert current_url == expected_url

    def check_header_visible(self):
        assert self.cases_page.header_became_visible()

    def check_query_parameter(self, param, value):
        assert self.cases_page.query_parameter_matches(param, value)

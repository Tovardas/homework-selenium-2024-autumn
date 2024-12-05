class SurveysPageVerification:
    def __init__(self, surveys_page):
        self.surveys_page = surveys_page

    def check_last_image_name(self, file_path):
        assert self.surveys_page.get_last_image_name_from_media_library() == os.path.basename(file_path)

    def check_1_errors_empty(self, message):
        assert self.surveys_page.check_1_errors_empty(message)

    def check_1_errors_all(self, message):
        assert self.surveys_page.check_1_errors_all(message)

    def check_2_error_empty(self):
        assert self.surveys_page.check_2_error_empty()

    def check_3_error_empty(self, message):
        assert self.surveys_page.check_3_error_empty(message)

    def check_3_errors_all(self, message):
        assert self.surveys_page.check_3_errors_all(message)

    def check_3_errors_link(self, message):
        assert self.surveys_page.check_3_errors_link(message)

    def check_url_opened(self, url):
        assert self.surveys_page.driver.current_url == url

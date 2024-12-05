class ForumPageVerification:
    def __init__(self, forum_page):
        self.forum_page = forum_page

    def check_page_title(self, expected_title):
        assert self.forum_page.get_page_title() == expected_title

    def check_url_opened(self, expected_url):
        assert self.forum_page.driver.current_url == expected_url

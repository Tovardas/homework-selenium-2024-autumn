import pytest

from ui.pages.base_page import PageNotOpenedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseCase:
    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

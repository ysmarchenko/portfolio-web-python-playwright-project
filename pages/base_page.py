from playwright.sync_api import Page


class BasePage:
    default_timeout = 10

    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_button = "(//*[text()='Accept all'])[1]"

    def wait_element_visible(self, selector: str) -> None:
        try:
            locator = self.page.locator(selector)
            locator.wait_for(state="visible", timeout=self.default_timeout * 1000)
        except Exception as e:
            raise Exception(f"Error while waiting for element '{selector}' to become visible: {str(e)}")

    def click_on_element(self, selector: str) -> None:
        try:
            self.wait_element_visible(selector)
            self.page.locator(selector).click()
        except Exception as e:
            raise Exception(f"Error while clicking on the element: {str(e)}")

    def get_text(self, selector: str) -> str:
        try:
            self.wait_element_visible(selector)
            return self.page.locator(selector).inner_text()
        except Exception as e:
            raise Exception(f"Error while getting text from the element: {str(e)}")

    def clear_field(self, selector: str) -> None:
        try:
            self.wait_element_visible(selector)
            locator = self.page.locator(selector)
            locator.clear()
        except Exception as e:
            raise Exception(f"Error while clearing the field: {str(e)}")

    def fill_field(self, selector: str, text: str) -> None:
        try:
            self.clear_field(selector)
            locator = self.page.locator(selector)
            locator.fill(text)
        except Exception as e:
            raise Exception(f"Error while filling the field: {str(e)}")

    def click_accept_cookies_button(self):
        self.click_on_element(self.accept_cookies_button)

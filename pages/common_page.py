from base_page import BasePage
from data.enums import Tabs, Languages, DropdownTypes

class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # -----------------------------------------------------------
    #   ELEMENTS
    # -----------------------------------------------------------
    def select_translate_tab(self, tab_name: Tabs) -> str:
        return f"button[aria-label='{tab_name.value} translation']"

    def tab_selector(self, tab_name: Tabs) -> str:
        return f"//h1[text()='{tab_name.value} translation']/following-sibling::div"

    def more_languages(self, dropdown_type: DropdownTypes) -> str:
        if dropdown_type == DropdownTypes.FROM:
            return '//*[@aria-label="More source languages"]'
        elif dropdown_type == DropdownTypes.TO:
            return '//*[@aria-label="More target languages"]'

    def select_language_tab(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> str:
        return f"{self.tab_selector(tab_name)}{self.more_languages(dropdown_type)}/ancestor::div[1]//span[text()='{language.value}']/ancestor::button"

    def selected_language(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> str:
        return f"{self.tab_selector(tab_name)}{self.more_languages(dropdown_type)}/ancestor::div[1]//span[text()='{language.value}']/ancestor::span[1]/following-sibling::span/span"

    def open_languages_dropdown(self, tab_name: Tabs, dropdown_type: DropdownTypes) -> str:
        return f"{self.tab_selector(tab_name)}{self.more_languages(dropdown_type)}"

    def swap_languages_button(self, tab_name: Tabs) -> str:
        return f"{self.tab_selector(tab_name)}//button[contains(@aria-label, 'Swap languages')]"

    def search_languages_input(self, tab_name: Tabs, dropdown_type: DropdownTypes) -> str:
        return f"{self.tab_selector(tab_name)}//div[text()='Translate {dropdown_type.value.lower()}']//ancestor::div[2]//input[@placeholder='Search languages']"

    def search_language_option(self, language: Languages) -> str:
        return f"//input[@aria-label='Search languages']/ancestor::div[2]//span[text()='{language.value}']"

    # -----------------------------------------------------------
    #   STEP FUNCTIONS
    # -----------------------------------------------------------
    def check_element_color(self, element, expected_color: str) -> None:
        element_color = element.evaluate('el => getComputedStyle(el).borderColor')
        assert element_color == expected_color, f"Expected color {expected_color}, but got {element_color}"

    def click_google_translate_tab(self, tab_name: Tabs) -> None:
        tab = self.page.locator(self.select_translate_tab(tab_name))
        self.wait_element_visible(self.select_translate_tab(tab_name))
        tab.click()

    def check_selected_language(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages, color: str = '#1a73e8') -> None:
        selected_lang_elem = self.page.locator(self.selected_language(tab_name, dropdown_type, language))
        self.wait_element_visible(self.selected_language(tab_name, dropdown_type, language))
        assert selected_lang_elem.evaluate('el => getComputedStyle(el).color') == color

    def click_language_tab(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> None:
        language_tab = self.page.locator(self.select_language_tab(tab_name, dropdown_type, language))
        self.wait_element_visible(self.select_language_tab(tab_name, dropdown_type, language))
        language_tab.click()
        self.check_selected_language(tab_name, dropdown_type, language, '#174ea6')

    def click_swap_languages(self, tab_name: Tabs) -> None:
        swap_button = self.page.locator(self.swap_languages_button(tab_name))
        self.wait_element_visible(self.swap_languages_button(tab_name))
        swap_button.click()

    def search_and_select_language(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> None:
        self.page.locator(self.open_languages_dropdown(tab_name, dropdown_type)).click()
        self.wait_element_visible(self.search_languages_input(tab_name, dropdown_type))
        search_input = self.page.locator(self.search_languages_input(tab_name, dropdown_type))
        search_input.fill(language.value)
        self.page.locator(self.search_language_option(language)).click()
        self.check_selected_language(tab_name, dropdown_type, language)

    def select_from_to_languages(self, tab_name: Tabs, from_language: Languages, to_language: Languages) -> None:
        self.search_and_select_language(tab_name, DropdownTypes.FROM, from_language)
        self.search_and_select_language(tab_name, DropdownTypes.TO, to_language)

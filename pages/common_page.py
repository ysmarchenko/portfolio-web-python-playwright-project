import time
from typing import Optional
from pages.base_page import BasePage
from data.enums import Tabs, Languages, DropdownTypes

selected_tab_color = "rgb(26, 115, 232)"

class CommonPage(BasePage):
    def __init__(self, base_page):
        super().__init__(base_page)

    # -----------------------------------------------------------
    #   ELEMENTS
    # -----------------------------------------------------------
    def select_translate_tab(self, tab_name: Tabs) -> str:
        return f"button[aria-label='{tab_name} translation']"

    def tab_selector(self, tab_name: Tabs) -> str:
        return f"//h1[text()='{tab_name} translation']/following-sibling::div"

    def more_languages(self, dropdown_type: DropdownTypes) -> Optional[str]:
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
        self.click_on_element(self.select_translate_tab(tab_name))

    def check_selected_language(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> None:
        selected_lang_elem = self.page.locator(self.selected_language(tab_name, dropdown_type, language))
        self.click_google_translate_tab(tab_name)
        self.check_element_color(selected_lang_elem, selected_tab_color)

    def click_language_tab(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> None:
        self.click_on_element(self.select_language_tab(tab_name, dropdown_type, language))
        self.check_selected_language(tab_name, dropdown_type, language)

    def click_swap_languages(self, tab_name: Tabs) -> None:
        self.click_on_element(self.swap_languages_button(tab_name))

    def search_and_select_language(self, tab_name: Tabs, dropdown_type: DropdownTypes, language: Languages) -> None:
        self.click_on_element(self.open_languages_dropdown(tab_name, dropdown_type))
        self.fill_field(self.search_languages_input(tab_name, dropdown_type), language.value)
        self.click_on_element(self.search_language_option(language))
        self.check_selected_language(tab_name, dropdown_type, language)

    def select_from_to_languages(self, tab_name: Tabs, from_language: Languages, to_language: Languages) -> None:
        self.search_and_select_language(tab_name, DropdownTypes.FROM, from_language)
        time.sleep(1) # Need to wait 1 second due to the animation, there is no other way to handle animation
        self.search_and_select_language(tab_name, DropdownTypes.TO, to_language)

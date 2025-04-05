import pytest
from data.enums import Tabs, Languages, DropdownTypes
from pages.common_page import CommonPage

tab_names = [tab.value for tab in Tabs]

@pytest.mark.usefixtures('base_page')
class TestSelectLanguage:

    @pytest.fixture
    def common_page(self, base_page):
        return CommonPage(base_page.page)

    @pytest.mark.parametrize("tab", tab_names)
    def test_select_languages_by_click_on_header(self, common_page, tab):
        common_page.click_google_translate_tab(tab)
        common_page.click_language_tab(tab, DropdownTypes.FROM, Languages.ENGLISH)
        common_page.click_language_tab(tab, DropdownTypes.TO, Languages.SPANISH)

    @pytest.mark.parametrize("tab", tab_names)
    def test_search_and_select_languages(self, common_page, tab):
        common_page.click_google_translate_tab(tab)
        common_page.search_and_select_language(tab, DropdownTypes.FROM, Languages.ENGLISH)
        common_page.search_and_select_language(tab, DropdownTypes.TO, Languages.SPANISH)

    @pytest.mark.parametrize("tab", tab_names)
    def test_swap_languages_button(self, common_page, tab):
        common_page.click_google_translate_tab(tab)
        common_page.select_from_to_languages(tab, Languages.ENGLISH, Languages.SPANISH)
        common_page.click_swap_languages(tab)
        common_page.check_selected_language(tab, DropdownTypes.TO, Languages.ENGLISH)
        common_page.check_selected_language(tab, DropdownTypes.FROM, Languages.SPANISH)

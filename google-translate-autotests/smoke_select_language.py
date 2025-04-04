import pytest

@pytest.mark.usefixtures('base_page')
class TestSelectLanguage:

    @pytest.mark.web
    def test_click_on_element(self, base_page):
        base_page.click_on_element('xpath=(//*[.="Accept all"])[1]')

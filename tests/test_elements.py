import time
import pytest
from pom.homepage import Homepage
from pom.elementspage import Elementspage, Textboxpage, Checkboxpage, Radiobuttonpage


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_text_box(self):
        homepage = Homepage(self.driver)
        homepage.get_elements_card().click()
        elementspage = Elementspage(self.driver)
        elementspage.get_text_box_button().click()

        textboxpage = Textboxpage(self.driver)
        textboxpage.get_full_name_box().send_keys('Andre Moris')
        textboxpage.get_email_box().send_keys('abc@mail.com')
        textboxpage.get_current_address_box().send_keys('2311 North Los Robles Avenue')
        textboxpage.get_permanent_address_box().send_keys('2311 North Los Robles Avenue')
        textboxpage.get_submit_button().click()
        time.sleep(2)

    def test_check_box(self):
        homepage = Homepage(self.driver)
        homepage.get_elements_card().click()
        elementspage = Elementspage(self.driver)
        elementspage.get_check_box_button().click()

        checkboxpage = Checkboxpage(self.driver)
        checkboxpage.get_home_check_box().click()
        time.sleep(2)

    def test_radio_button(self):
        homepage = Homepage(self.driver)
        homepage.get_elements_card().click()
        elementspage = Elementspage(self.driver)
        elementspage.get_radio_button().click()

        radiobuttonpage = Radiobuttonpage(self.driver)
        radiobuttonpage.get_yes_radio_button().click()
        time.sleep(2)
        radiobuttonpage.get_imp_radio_button().click()
        time.sleep(2)

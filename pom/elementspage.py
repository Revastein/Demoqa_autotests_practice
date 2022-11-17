from base.baseclass import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class Elementspage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__text_box_button = '//*[@id="item-0"]'
        self.__check_box_button = '//*[@id="item-1"]'
        self.__radio_button = '//*[@id="item-2"]'
        self.__web_tables_button = '//*[@id="item-3"]'
        self.__buttons = '//*[@id="item-4"]'

    def get_text_box_button(self) -> WebElement:
        return self.is_visible('xpath', self.__text_box_button, 'Text box')

    def get_check_box_button(self) -> WebElement:
        return self.is_visible('xpath', self.__check_box_button, 'Check box')

    def get_radio_button(self) -> WebElement:
        return self.is_visible('xpath', self.__radio_button, 'Radio button')

    def get_web_tables_button(self) -> WebElement:
        return self.is_visible('xpath', self.__web_tables_button, 'Web tables')

    def get_buttons(self) -> WebElement:
        return self.is_visible('xpath', self.__buttons, 'Buttons')


class Textboxpage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__full_name_box = '//*[@id="userName"]'
        self.__email_box = '//*[@id="userEmail"]'
        self.__current_address_box = '//*[@id="currentAddress"]'
        self.__permanent_address_box = '//*[@id="permanentAddress"]'
        self.__submit_button = '//*[@id="submit"]'

    def get_full_name_box(self) -> WebElement:
        return self.is_visible('xpath', self.__full_name_box, 'Full name box')

    def get_email_box(self) -> WebElement:
        return self.is_visible('xpath', self.__email_box, 'Email box')

    def get_current_address_box(self) -> WebElement:
        return self.is_visible('xpath', self.__current_address_box, 'Current address box')

    def get_permanent_address_box(self) -> WebElement:
        return self.is_visible('xpath', self.__permanent_address_box, 'Permanent address box')

    def get_submit_button(self) -> WebElement:
        return self.is_visible('xpath', self.__submit_button, 'Submit button')


class Checkboxpage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__home_check_box = '//*[@id="tree-node"]/ol/li/span/label'

    def get_home_check_box(self) -> WebElement:
        return self.is_visible('xpath', self.__home_check_box, 'Home check box')


class Radiobuttonpage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__yes_radio_button = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label'
        self.__imp_radio_button = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label'

    def get_yes_radio_button(self) -> WebElement:
        return self.is_visible('xpath', self.__yes_radio_button, 'Yes radio button')

    def get_imp_radio_button(self) -> WebElement:
        return self.is_visible('xpath', self.__imp_radio_button, 'Impressive radio button')

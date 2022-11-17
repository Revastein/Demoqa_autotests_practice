from base.baseclass import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class Homepage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__elements_card = '//*[@id="app"]/div/div/div[2]/div/div[1]'
        self.__forms_card = '//*[@id="app"]/div/div/div[2]/div/div[2]'
        self.__alerts_card = '//*[@id="app"]/div/div/div[2]/div/div[3]'
        self.__widgets_card = '//*[@id="app"]/div/div/div[2]/div/div[4]'
        self.__interactions_card = '//*[@id="app"]/div/div/div[2]/div/div[5]'
        self.__book_store_card = '//*[@id="app"]/div/div/div[2]/div/div[6]'

    def get_elements_card(self) -> WebElement:
        return self.is_visible('xpath', self.__elements_card, 'Element card')

    def get_forms_card(self) -> WebElement:
        return self.is_visible('xpath', self.__forms_card, 'Forms card')

    def get_alerts_card(self) -> WebElement:
        return self.is_visible('xpath', self.__alerts_card, 'Alerts card')

    def get_widgets_card(self) -> WebElement:
        return self.is_visible('xpath', self.__widgets_card, 'Widgets card')

    def get_interactions_card(self) -> WebElement:
        return self.is_visible('xpath', self.__interactions_card, 'Interactions card')

    def get_book_store_card(self) -> WebElement:
        return self.is_visible('xpath', self.__book_store_card, 'Book store card')
    
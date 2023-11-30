from selenium.webdriver import ActionChains
from locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def open_main_page(self):
        self.open_page()

    def click_temperature_button(self):
        button = self.element_is_clickable(MainPageLocators.TEMPERATURE_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.click(button)
        actions.perform()

    def click_length_button(self):
        button = self.element_is_present(MainPageLocators.LENGTH_BUTTON)
        button.click()

    def click_weight_button(self):
        button = self.element_is_present(MainPageLocators.WEIGHT_BUTTON)
        button.click()

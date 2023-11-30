from .base_page import BasePage
from selenium.webdriver.support.select import Select
from locators import TemperatureConversionPageLocators as TempLoc
from locators import LengthConversionPageLocators as SelectLoc
from locators import WeightConversionPageLocators as Loc


class SelectPage(BasePage):
    def select_option_celsius(self):
        select_elem = Select(self.element_is_visible(TempLoc.TEMPERATURE_FROM_SELECT))
        select_elem.select_by_visible_text('Celsius')

    def select_option_fahrenheit(self):
        select_elem = Select(self.element_is_visible(TempLoc.TEMPERATURE_TO_SELECT))
        select_elem.select_by_visible_text('Fahrenheit')

    def select_option_meters(self):
        select_elem = Select(self.element_is_visible(SelectLoc.LENGTH_FROM_SELECT))
        select_elem.select_by_visible_text('Meters')

    def select_option_feet(self):
        select_elem = Select(self.element_is_visible(SelectLoc.LENGTH_TO_SELECT))
        select_elem.select_by_visible_text('Feet')

    def select_option_ounces(self):
        select_elem = Select(self.element_is_visible(Loc.WEIGHT_FROM_SELECT))
        select_elem.select_by_visible_text('Ounces')

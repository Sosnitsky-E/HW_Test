from .base_page import BasePage
from pages.generator import RandomNum
from locators import LengthConversionPageLocators as Loc
from locators import WeightConversionPageLocators as WeightLoc


class InputPage(BasePage):

    # The method generates a random number for input into the converter.
    def fill_input(self):
        num = RandomNum.random_num()
        self.fill_in_field(Loc.ARGUMENT_CONV_INPUT, num)
        return num

    # The method that receives the response text after conversion.
    def get_answer(self):
        return self.get_text(Loc.ANSWER)

    # The method converts a temperature value from Celsius to Fahrenheit.
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    # The method converts a length value from meters to feet.
    def meters_to_feet(self, meters):
        return meters * 3.28084

    def fill_input_value_grams(self):
        self.fill_in_field(WeightLoc.WEIGHT, 'grams')

    def click_btn_convert(self):
        self.action_move_to_element_click(WeightLoc.CONVERT_BTN)

    # The method converts a weight value from ounces to grams.
    def ounces_to_grams(self, ounces):
        return ounces * 28.3495231

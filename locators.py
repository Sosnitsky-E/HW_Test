from selenium.webdriver.common.by import By


class MainPageLocators:
    TEMPERATURE_BUTTON = By.CSS_SELECTOR, ".typeConv.temperature.bluebg"
    WEIGHT_BUTTON = By.CSS_SELECTOR, ".typeConv.weight.bluebg"
    LENGTH_BUTTON = By.CSS_SELECTOR, ".typeConv.length.bluebg"


class TemperatureConversionPageLocators:
    TEMPERATURE_FROM_SELECT = By.CSS_SELECTOR, "#unitFrom"
    TEMPERATURE_TO_SELECT = By.CSS_SELECTOR, "#unitTo"
    ANSWER = By.CSS_SELECTOR, "#answer"


class LengthConversionPageLocators:
    LENGTH_FROM_SELECT = By.CSS_SELECTOR, "#unitFrom"
    LENGTH_TO_SELECT = By.CSS_SELECTOR, "#unitTo"
    ARGUMENT_CONV_INPUT = By.CSS_SELECTOR, "#argumentConv"
    ANSWER = By.CSS_SELECTOR, "#answer"


class WeightConversionPageLocators:
    WEIGHT_FROM_SELECT = By.CSS_SELECTOR, "#unitFrom"
    WEIGHT = By.CSS_SELECTOR, "#queryTo"
    INPUT_WEIGHT_GRAM = By.CSS_SELECTOR, "#results > ol > li:nth-child(1) > div > input"
    CONVERT_BTN = By.CSS_SELECTOR, "#results > ol > li:nth-child(1) > div > a:nth-child(3)"
    ARGUMENT_CONV_INPUT = By.CSS_SELECTOR, "#argumentConv"
    ANSWER = By.CSS_SELECTOR, "#answer"

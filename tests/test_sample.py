from data import PageLinks
from pages.main_page import MainPage
from pages.select_page import SelectPage
from pages.input_page import InputPage


class TestConvertsTemperature:
    # Navigates to the main page, clicks on the temperature button, selects Celsius and Fahrenheit options.
    # Verifies that the URL contains "celsius-to-fahrenheit."
    # test_verify_converts_temperature_celsius_to_fahrenheit method:
    def test_verify_url_converts_temperature_celsius_to_fahrenheit(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_temperature_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_celsius()
        select_page.select_option_fahrenheit()
        assert "celsius-to-fahrenheit" in select_page.get_actual_url_of_current_page()

    # Similar to the first method but additionally interacts with the input and output fields.
    # Fills the input field, retrieves the output value, and asserts the correctness of the conversion.
    def test_verify_converts_temperature_celsius_to_fahrenheit(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_temperature_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_celsius()
        select_page.select_option_fahrenheit()
        input_page = InputPage(driver, main_page.get_actual_url_of_current_page())
        input_value = input_page.fill_input()
        output_value = input_page.get_answer()
        assert str(input_value) == output_value[:2]
        assert output_value[6:10] in str(float(input_page.celsius_to_fahrenheit(input_value)))


class TestConvertsMetersToFeet:
    # Navigates to the main page, clicks on the length button, selects meters and feet options.
    # Verifies that the URL contains "meters-to-feet"
    def test_verify_url_converts_meters_to_feet(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_length_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_meters()
        select_page.select_option_feet()
        assert "meters-to-feet" in select_page.get_actual_url_of_current_page()

    # Similar to the first method but additionally interacts with the input and output fields.
    # Fills the input field, retrieves the output value, and asserts the correctness of the conversion.
    def test_verify_converts_meters_to_feet(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_length_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_meters()
        select_page.select_option_feet()
        input_page = InputPage(driver, main_page.get_actual_url_of_current_page())
        input_value = input_page.fill_input()
        output_value = input_page.get_answer()
        assert str(input_value) == output_value[:2]
        assert output_value[5:7] in str(int(input_page.meters_to_feet(input_value)))


class TestConvertsOuncesToGrams:
    # Navigates to the main page, clicks on the weight button, selects ounces option.
    # Fills the input value as 'grams', clicks the convert button, and verifies that the URL contains "ounces-to-grams."
    def test_verify_url_converts_ounces_to_grams(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_weight_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_ounces()
        input_page = InputPage(driver, main_page.get_actual_url_of_current_page())
        input_page.fill_input_value_grams()
        input_page.click_btn_convert()
        assert "ounces-to-grams" in input_page.get_actual_url_of_current_page()

    # Similar to the first method but additionally interacts with the input and output fields.
    # Fills the input value, clicks the convert button, retrieves the output value,
    # and asserts the correctness of the conversion.
    def test_verify_converts_ounces_to_grams(self, driver):
        main_page = MainPage(driver, PageLinks.MAIN_PAGE_URL)
        main_page.open_main_page()
        main_page.click_weight_button()
        select_page = SelectPage(driver, main_page.get_actual_url_of_current_page())
        select_page.select_option_ounces()
        input_page = InputPage(driver, main_page.get_actual_url_of_current_page())
        input_page.fill_input_value_grams()
        input_page.click_btn_convert()
        input_value = input_page.fill_input()
        output_value = input_page.get_answer()
        assert str(input_value) == output_value[:2]
        assert str(input_page.ounces_to_grams(input_value))[:-4] in output_value[6:-2]

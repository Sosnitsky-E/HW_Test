import pytest
from datetime import datetime
from api_weather import WeatherApi
from info_weather import WeatherInfo


@pytest.mark.parametrize("zip_code", ["20852"])  # Test parameters
def test_weather(zip_code):
    current_month = datetime.now().month

    weather_api = WeatherApi()
    weather_data = weather_api.get_weather_by_zipcode(zip_code)

    # Statement: Weather data must be obtained
    assert weather_data is not None, "Failed to retrieve weather data."

    # Instantiating WeatherInfo and getting the temperature
    weather_info = WeatherInfo(weather_data)
    actual_temp = weather_info.get_temperature()
    expected_temp_min = weather_info.get_min_temperature()
    expected_temp_max = weather_info.get_max_temperature()

    # Statement: temperature must be the answer
    assert actual_temp is not None, "Temperature not found in response."

    # We calculate the permissible temperature range taking into account 10% fluctuations
    if expected_temp_min < 0:
        adjusted_min_temp = expected_temp_min * 1.1  # 10% lower for negative temperatures
    else:
        adjusted_min_temp = expected_temp_min * 0.9  # 10% lower for positive temperature

    if expected_temp_max < 0:
        adjusted_max_temp = expected_temp_max * 0.9  # 10% higher for negative temperature
    else:
        adjusted_max_temp = expected_temp_max * 1.1  # 10% higher for positive temperature

    # Statement: The actual temperature must be within the acceptable range
    assert adjusted_min_temp <= actual_temp <= adjusted_max_temp, \
        (f"Test failed. Current temperature {actual_temp}°C is not within the expected range "
         f"for month {current_month}: {adjusted_min_temp}°C - {adjusted_max_temp}°C.")

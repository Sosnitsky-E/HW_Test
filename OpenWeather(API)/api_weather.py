import requests


class WeatherApi:
    def __init__(self):
        # Primary URL for the weather API and API key derived from environment variables
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = "b6f6e0909f9015302989a3cffeec09f5"

    def get_weather_by_zipcode(self, zip_code):
        # Request parameters including zip code and API key.
        # Uses 'metric' unit to obtain temperature in degrees Celsius
        params = {
            'zip': f"{zip_code},us",
            'appid': self.api_key,
            'units': 'metric',
        }
        try:
            # Sending a request to the API
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # response code checking
            return response.json()
        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            return None

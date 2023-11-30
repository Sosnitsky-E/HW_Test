class WeatherInfo:
    def __init__(self, data):
        # Initialization with weather data
        self.data = data

    def get_temperature(self):
        # Returns the current temperature from weather data
        return self.data.get('main', {}).get('temp')

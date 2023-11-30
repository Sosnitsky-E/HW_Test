# Homework Project Instructions

As part of our hiring process, we include a homework project that we would like you to accomplish. Please complete the assignment independently and deploy it to us via git (you can open a free account on platforms like GitHub or GitLab) or any other cloud storage service of your choice.

## Project Overview

The purpose of this short project is to write automation scripts for the website [Metric Conversions](https://www.metric-conversions.org/).

### Technical Requirements:

- The project can be implemented in **Python**, **C#**, or **Java**.
- Use **Selenium** as the testing framework, with **Chrome** as the browser.

###  Automation Web Site Testing:

Please create tests that perform the following conversions:
1. **Celsius to Fahrenheit**: Create a test that converts Celsius temperature to Fahrenheit temperature.
2. **Meters to Feet**: Create a test that converts meters to feet.
3. **Ounces to Grams**: Create a test that converts ounces to grams.

### API Testing:

For the API testing part, create a test that retrieves the weather forecast for zip code **20852** in the USA:
- **Get the weather**: Fetch the weather from [OpenWeatherMap](https://openweathermap.org/) for zip code 20852.
- **Run the test**: Execute the test that retrieves the weather for this zip code.
- **Verify the results**: Ensure that the results are within a 10% range of the expected outcome.


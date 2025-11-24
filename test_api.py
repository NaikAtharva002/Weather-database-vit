import weather_api
import json

def test_api():
    city = "Bhopal"
    print(f"Testing API for {city}...")
    
    # Test Current Weather
    current = weather_api.get_current_weather(city)
    if current:
        print("Current Weather: Success")
        print(f"Temp: {current['current']['temp_c']}°C")
    else:
        print("Current Weather: Failed")

    # Test Forecast
    forecast = weather_api.get_forecast(city)
    if forecast:
        print("Forecast: Success")
        print(f"Forecast Days: {len(forecast['forecast']['forecastday'])}")
    else:
        print("Forecast: Failed")

if __name__ == "__main__":
    test_api()

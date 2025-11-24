import requests
import config

def get_current_weather(city):
    """
    Fetches current weather data for a given city.
    """
    url = f"{config.BASE_URL}/current.json"
    params = {
        "key": config.API_KEY,
        "q": city
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current weather: {e}")
        return None

def get_forecast(city, days=7):
    """
    Fetches forecast data for a given city for the next 'days' days.
    """
    url = f"{config.BASE_URL}/forecast.json"
    params = {
        "key": config.API_KEY,
        "q": city,
        "days": days,
        "aqi": "no",
        "alerts": "yes"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast: {e}")
        return None

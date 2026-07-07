import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("weather_api_key")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_current_weather(location):
    url = f"{BASE_URL}/weather"
    params = {"appid": API_KEY, "q": location, "units": "metric"}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    return {
        "location": data.get("name"),
        "temperature": data.get("main", {}).get("temp"),
        "condition": data.get("weather", [{}])[0].get("description"),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
        "pressure": data.get("main", {}).get("pressure"),
        "sunrise": data.get("sys", {}).get("sunrise"),
        "sunset": data.get("sys", {}).get("sunset"),

    }




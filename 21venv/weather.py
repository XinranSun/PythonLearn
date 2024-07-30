import os

import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


#
#
def get_current_weather():
    print("Getting current weather")
    city = input("\nEnter your city name: \n")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&lang=zh_cn&units=metric"
    weather_data = requests.get(request_url).json()
    # pprint(weather_data)
    print(
        f"\nCurrent city is: {weather_data['name']},\nCurrent temp is : {weather_data['main']['temp']},\nCurrent "
        f"feel_like is: {weather_data['main']['feels_like']}")


if __name__ == "__main__":
    get_current_weather()

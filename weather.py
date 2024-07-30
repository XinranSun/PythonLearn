from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city='tangshan'):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&lang=zh_cn&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == '__main__':
    print("\n ****Getting current weather data ****\n")

    city = input("Enter your city name: \n")
    weather_data = get_current_weather(city)
    print("\n ****Getting")
    pprint(weather_data)

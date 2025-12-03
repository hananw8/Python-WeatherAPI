import requests
from dotenv import load_dotenv
import os

load_dotenv()

class City:
    def __init__(self, name, lat, lon, units = "metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Add OPENWEATHER_API_KEY=... to your .env file.")

        self.get_data()

    def get_data(self): 
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={self.api_key}")
        except:
            print("No internet connection :(")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp} ° {units_symbol}")
        print(f"Today's High: {self.temp_min} ° {units_symbol}")
        print(f"Today's Low: {self.temp_max} ° {units_symbol}")
        print()

my_city = City("London", 51.50722, -0.1275)
my_city.temp_print()

vac_city = City("Tokyo", 35.6762, 139.6503)
vac_city.temp_print()
import requests
import json
holidays = []
print("Getting Holiday Info...")
holiday_api_url = "https://holidayapi.com/v1/holidays?pretty&key=7ebcf0af-6d7c-41a0-b3e3-28efe08d5fd7&country=CA&year=2020"
h_info = requests.get(holiday_api_url).json()["holidays"]
for holiday in h_info:
  holidays.append(holiday["date"])
  print(holiday["date"])

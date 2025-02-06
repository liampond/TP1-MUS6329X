import requests
import os
from dotenv import load_dotenv

load_dotenv()

location = "45.509379%2C%20-73.608654"
api_key = os.getenv("api_key")

url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)

print(response.text)
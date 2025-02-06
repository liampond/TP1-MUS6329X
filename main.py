import requests
import os
import json 
from dotenv import load_dotenv
from pythonosc import udp_client

load_dotenv()

location = "45.509379%2C%20-73.608654"
api_key = os.getenv("tomorrowio_apikey")
if not api_key:
    raise ValueError("API key not found! Please set it in your .env file under 'tomorrowio_apikey'.")

# Set up OSC client to send messages to Max on port 8000
client = udp_client.SimpleUDPClient("127.0.0.1", 8000)

url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Error fetching data:", response.status_code)
    print("Response text:", response.text)
    exit(1)

try:
    data = response.json()
except ValueError:
    print("Error decoding JSON")
    exit(1)

print("Response JSON:")
print(json.dumps(data, indent=2))

try:
    temperature = data["data"]["values"]["temperature"]
    humidity    = data["data"]["values"]["humidity"]
    windSpeed   = data["data"]["values"]["windSpeed"]
except KeyError as e:
    print("Error accessing data:", e)
    exit(1)

print(f"Temperature: {temperature}, Humidity: {humidity}, Wind Speed: {windSpeed}")

# Send values to Max using OSC
client.send_message("/weather/temperature", temperature)
client.send_message("/weather/humidity", humidity)
client.send_message("/weather/windSpeed", windSpeed)

import time
import requests
import os
import json
from dotenv import load_dotenv
from pythonosc import udp_client

def main():
    load_dotenv()
    
    location = "45.509379%2C%20-73.608654"
    api_key = os.getenv("tomorrowio_apikey")
    if not api_key:
        raise ValueError("API key not found! Please set it in your .env file under 'tomorrowio_apikey'.")
    
    client = udp_client.SimpleUDPClient("127.0.0.1", 8000)
    
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"
    headers = {
        "accept": "application/json",
        "accept-encoding": "deflate, gzip, br"
    }
    
    # Query the API once per minute, for five minutes
    for i in range(5):
        print(f"\n--- Query iteration {i + 1} ---")
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            print("Response text:", response.text)
        else:
            try:
                data = response.json()
            except ValueError:
                print("Error decoding JSON")
                continue

            print("Response JSON:")
            print(json.dumps(data, indent=2))

            try:
                temperature = data["data"]["values"]["temperature"]
                humidity    = data["data"]["values"]["humidity"]
                windSpeed   = data["data"]["values"]["windSpeed"]
            except KeyError as e:
                print("Error accessing data:", e)
                continue

            print(f"Temperature: {temperature}, Humidity: {humidity}, Wind Speed: {windSpeed}")

            # Send values to Max using OSC
            client.send_message("/weather/temperature", temperature)
            client.send_message("/weather/humidity", humidity)
            client.send_message("/weather/windSpeed", windSpeed)
        
        if i < 4:
            print("Waiting for 60 seconds...\n")
            time.sleep(60)
            
if __name__ == "__main__":
    main()

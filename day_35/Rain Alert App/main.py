import os
from dotenv import load_dotenv
import requests
import geocoder
from twilio.rest import Client

load_dotenv()

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def get_current_coordinates():
        global MY_LAT
        global MY_LONG

        try:
            # Use 'ip("me")' to get location based on your IP address
            g = geocoder.ip("me")

            if g.ok:
                MY_LAT = g.latlng[0]
                MY_LONG = g.latlng[1]
                print(f"Current Latitude: {MY_LAT}")
                print(f"Current Longitude: {MY_LONG}")
                return MY_LAT, MY_LONG
            else:
                print("Could not retrieve location information.")
                return None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

get_current_coordinates()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon" : MY_LONG,
    "appid": os.getenv("OPEN_WEATHER_API"),
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    for data in hour_data['weather']:
        condition_code = data['id']
        if int(condition_code) < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella.")
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    # body="It's going to rain today. Remember to bring an ☔",
    # from_="+15023830449",
    # to="+15023830449",
    # )

    # print(message.status)
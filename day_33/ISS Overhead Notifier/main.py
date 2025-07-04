import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def lookup_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:🚀 The ISS is Above You Right Now!\n\nJust a quick heads-up—look up! 👀\nThe International Space Station is currently flying over your location. If the skies are clear, you might be able to spot it as a fast-moving bright light traveling west to east.")

#If the ISS is close to my current position
if iss_latitude in range(MY_LAT-5, MY_LAT+6):
    if iss_longitude in range(MY_LONG, MY_LONG+6):
        if time_now.hour >= sunset:
            lookup_email()
            
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




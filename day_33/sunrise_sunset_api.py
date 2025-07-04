import requests
from datetime import datetime

MY_LAT = 51.587351
MY_LNG = -0.127758

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
}

reponse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunrise)

time_now = datetime.now()
print(time_now.hour)
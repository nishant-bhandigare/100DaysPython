import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_AUTHENTICATION")
user_input = input("Tell me which exerciese you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/"
sheety_endpoint = "https://api.sheety.co/"
sheety_username = "8ab1c9d13ab9a60abf0150566b5f7a4a"
sheety_project_name = "myWorkouts"
sheety_sheet_name = "workouts"

query = {
    "query": user_input,
}

nutritionix_headers = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY,
}

response = requests.post(url=f"{nutritionix_endpoint}v2/natural/exercise", headers=nutritionix_headers, json=query)
response.raise_for_status()
workout_data = response.json()
# print(workout_data)

now = datetime.now()

# date = now.strftime(r"%-d/%-m/%Y")
# time = now.strftime(r"%H:%M:%S")

date = now.strftime("%#d/%#m/%Y")  # Windows-friendly version
time = now.strftime("%H:%M:%S")

workout_stats = {
    "workout":{
        "date": date,
        "time": time,
        "exercise": workout_data['exercises'][0]['name'].title(),
        "duration": workout_data['exercises'][0]['duration_min'],
        "calories": workout_data['exercises'][0]['nf_calories'],
    }    
}

# print(workout_stats)

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

response = requests.post(url=f"{sheety_endpoint}/{sheety_username}/{sheety_project_name}/{sheety_sheet_name}", headers=sheety_headers, json=workout_stats)
response.raise_for_status()
print(response.status_code)
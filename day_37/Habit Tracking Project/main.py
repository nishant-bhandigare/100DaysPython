import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = "thomasshelby"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("PIXELA"),
    "username": 'thomasshelby',
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA"),
}

# CREATE A GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_data = {
    "date": today.strftime(r"%Y%m%d"),
    "quantity": "1",
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
# POST A PIXEL
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
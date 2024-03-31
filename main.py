import requests
from constants import *
from datetime import datetime
from processing import *
response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=20)
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS, timeout=20)
sunset_response.raise_for_status()

sunset_data = sunset_response.json()

sunrise = hour_splitter(sunset_data["results"]["sunrise"])
sunset = hour_splitter(sunset_data["results"]["sunset"])

print(sunset)

time_now = datetime.now()

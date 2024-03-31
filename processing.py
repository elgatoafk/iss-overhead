import requests
from datetime import datetime
from constants import *
import smtplib
from sensitive import *
from email.message import EmailMessage


def hour_splitter(date_time: str) -> int:
    time_only = date_time.split("T")[1]
    hour = time_only.split(":")[0]
    return int(hour)


def get_iss_position() -> tuple:
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=20)
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    return longitude, latitude

def get_sunrise_sunset(parameters: dict) -> tuple:
    sunset_response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters, timeout=20
)
    sunset_response.raise_for_status()

    sunset_data = sunset_response.json()

    sunrise = hour_splitter(sunset_data["results"]["sunrise"])
    sunset = hour_splitter(sunset_data["results"]["sunset"])
    return sunrise, sunset

def is_dark():
    time_now = datetime.now()
    current_hour = time_now.hour
    sunrise_sunset = get_sunrise_sunset(PARAMETERS)
    return current_hour > sunrise_sunset[1] or current_hour < sunrise_sunset[0]

def is_iss_close():
    iss_position = get_iss_position()
    my_position = (MY_LONGITUDE, MY_LATITUDE)
    return (my_position[1] - 5 <= iss_position[1] <= my_position[1] + 5) and my_position[0] - 5 <= iss_position[0] <= my_position[0]+5


def send_notif():
    msg = EmailMessage()
    msg.set_content('Look up')

    msg['Subject'] = 'ISS is overhead'
    msg['From'] = my_email
    msg['To'] = other_email


    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.send_message(msg)
    connection.close()



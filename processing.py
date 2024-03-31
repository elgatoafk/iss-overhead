import requests

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

def hour_splitter(date_time: str) -> int:
    time_only = date_time.split("T")[1]
    hour = time_only.split(":")[0]
    return int(hour)
from processing import *
import time

while True:
    time.sleep(60)
    if is_dark() and is_iss_close():
        send_notif()



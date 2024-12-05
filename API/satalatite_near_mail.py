import requests
from datetime import datetime
import smtplib
import time
MY_LAT=27.7172
MY_LONG=85.3240
def iss_overhead():
    response1=requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response1.json()
    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"]) 
    response1.raise_for_status()
    iss_position=(iss_latitude,iss_longitude)
    current_time=data["timestamp"]
    print(f"current time is {current_time}")
    print(iss_position)
    if MY_LAT-5<= iss_latitude<=MY_LAT+5 and MY_LONG-5<= iss_longitude<=MY_LONG+5:
        return True
iss_overhead()
def is_night():
    parameters= {
        "lat":MY_LAT,
        "lng":MY_LONG, 
        "formatted":0,
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data2=response.json()
    sunrise=int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    print(sunrise)
    sunset=int(data2["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)
    time_now=datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True
is_night()
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        # Use environment variables for security
        EMAIL = os.environ.get("EMAIL")
        PASSWORD = os.environ.get("EMAIL_PASSWORD")
        
        if EMAIL and PASSWORD:  # Ensure credentials are available
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,  # Note: Changed `to_addr` to `to_addrs`, as that's the correct parameter name.
                    msg="Subject: Look Outside\n\nThe ISS is passing overhead. Look outside!"
                )

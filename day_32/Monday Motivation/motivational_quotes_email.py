import datetime as dt
import os
from dotenv import load_dotenv
import smtplib
import random

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")
nowDay = dt.datetime.now()

if nowDay==0:
    with open(r"day_32\Monday Motivation\quotes.txt", 'r') as file:
        quote = random.choice(file.readlines())

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Monday Motivation\n\n{quote}")
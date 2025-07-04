##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv
import pandas as pd

def sendWishes(receiver_name, receiver_email):
    letter_no = random.choice([1,2,3])
    message = ""

    with open(f"day_32\letter_templates\letter_{letter_no}.txt", "r") as file:
        content = file.read()
        message = content.replace("[NAME]", receiver_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiver_email, msg=message)

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

now = dt.datetime.now()
nowDate = now.day
nowMonth = now.month

birthdays = pd.read_csv(r"day_32\birthdays.csv")

for index, row in birthdays.iterrows():
    if row["month"] == nowMonth and row["day"] == nowDate:
        sendWishes(row["name"], row["email"])

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





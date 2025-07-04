import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()
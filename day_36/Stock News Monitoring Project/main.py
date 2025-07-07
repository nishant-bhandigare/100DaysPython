import os
from dotenv import load_dotenv
import requests
import smtplib
from twilio.rest import Client
from newsapi import NewsApiClient

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_parameters = {
    'q': COMPANY_NAME,
    "sources":'bbc-news',
    "apiKey": os.getenv("NEWSAPI")
}

stocks_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("ALPHAVANTAGE")
}

news_response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

stocks_response = requests.get(url="https://www.alphavantage.co/query", params=stocks_parameters)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()












## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


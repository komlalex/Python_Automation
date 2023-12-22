"""
This Python program sends good morning text messages to a particular number every morning
"""
import dotenv 
import schedule
import time 
import os
import requests

dotenv.load_dotenv()
PHONE_NUMBER = os.getenv("CONTACT")

def send_message():
    res = requests.post("http://textbelt.com/text", {
        "phone": PHONE_NUMBER,
        "message": "Alex, Good morning",
        "key": "textbelt"
    })

    print(res.json())


#schedule.every().day.at("11:15").do(send_message())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)


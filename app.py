import os
import time
import schedule
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "" # Add telegram bot token here

def func():
    try:
        url = "https://hirunews.lk/"

        # Send request
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract image URL
        image = soup.select_one(".image-wrp img")
        image_url = image["src"] if image else None

        lel = open("./text.txt","r+")
        check = lel.readline()
        
        if check != image_url:

            # Extract title
            title = soup.select_one(".card-title-v1")
            title_text = title.get_text(strip=True) if title else None

            # Extract description
            description = soup.select_one(".description")
            description_text = description.get_text(strip=True) if description else None

            # Extract time (second span inside .update-wrp-lg)
            time_span = soup.select_one(".update-wrp-lg span:nth-of-type(2)")
            time_text = time_span.get_text(strip=True) if time_span else None

            cap1 = f"📮 <b>{title_text}</b>"
            cap2 = f"✍️ {description_text} \n\n📅 {time_text} \n\n🇱🇰 Powered by hirunews.lk"


            tg1 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id=-1001530519480&photo={image_url}&caption={cap1}&parse_mode=html"
            tg2 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-1001530519480&text={cap2}&parse_mode=html"

            requests.get(tg1)
            requests.get(tg2)

            with open('./text.txt', 'w') as f:
                f.write(image_url)

    except Exception as e:
            print(e)
            pass

schedule.every(2).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)

import os
import time
import schedule
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "" # Add telegram bot token here

def func():
    try:
        URL = "https://www.hirunews.lk/local-news.php?pageID=1"
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")

        head = soup.select('.all-section-tittle')[0].text
        headurl = soup.select('.all-section-tittle')[0].find('a').get('href')
        thumburl = soup.select('.sc-image')[0].find('img').get('src')
        tim = soup.select('.middle-tittle-time')[0].text
        tim = tim.strip()

        lel = open("./text.txt","r+")
        check = lel.readline()
        
        if check != thumburl:

            page2 = requests.get(headurl)
            soup2 = BeautifulSoup(page2.text, "html.parser")

            details = soup2.select('#article-phara2')[0].text

            hed = head.strip()
            details = details.strip()

            if "(වීඩියෝ)" in hed:
                hed = hed.replace("(වීඩියෝ)", "")

            if "(ඡායාරූප)" in hed:
                hed = hed.replace("(ඡායාරූප)", "")

            cap1 = f"📮 <b>{hed}</b>"
            cap2 = f"✍️ {details} \n\n📅 {tim} \n\n🇱🇰 Powered by hirunews.lk"

            tg1 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id=-1001530519480&photo={thumburl}&caption={cap1}&parse_mode=html"
            tg2 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-1001530519480&text={cap2}&parse_mode=html"

            requests.get(tg1)
            requests.get(tg2)

            with open('./text.txt', 'w') as f:
                f.write(thumburl)

    except Exception as e:
            print(e)
            pass

schedule.every(3).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)


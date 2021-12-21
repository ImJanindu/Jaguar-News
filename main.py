import os
import time
import schedule
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "2048328361:AAFNNLD7e_ht6pEMCOJyyK2_rMKJNAGaCf0"


def func():
    try:
        URL = "https://www.hirunews.lk/local-news.php?pageID=1"
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")

        head = soup.select('.all-section-tittle')[0].text
        headurl = soup.select('.all-section-tittle')[0].find('a').get('href')
        thumburl = soup.select('.sc-image')[0].find('img').get('src')
        tim = soup.select('.middle-tittle-time')[0].text

        lel = open("./text.txt","r+")
        check = lel.readline()

        if check != thumburl:

            page2 = requests.get(headurl)
            soup2 = BeautifulSoup(page2.text, "html.parser")

            details = soup2.select('.main-article-section')[0].text

            hed = head.lstrip()
            details = details.rstrip()
            details = details.lstrip()

            if "(වීඩියෝ)" in hed:
                hed = hed.replace("(වීඩියෝ)", "")

            cap = f"📮 <b>{hed}</b>"

            det = f"✍️ {details} \n{tim} \n<b>@Hiru_News</b> 🇱🇰"
        
            tg1 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id=-1001530519480&photo={thumburl}&caption={cap}&parse_mode=html"

            tg2 = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-1001530519480&text={det}&parse_mode=html"

            requests.get(tg1)
            requests.get(tg2)

            with open('./text.txt', 'w') as f:
                f.write(thumburl)

    except:
        pass

schedule.every(2).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)


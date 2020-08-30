import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Crucial-DDR4-2400-192000-CL17/dp/B019FREJOQ/ref=sr_1_1_sspa?crid=CYXMMJMQ2ZMW&dchild=1&keywords=2400mhz+8gb+ram&qid=1598776359&sprefix=2400mhz+8g%2Caps%2C332&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNExVWlo0SlVEWlJSJmVuY3J5cHRlZElkPUEwMzAxODc5MTlPRDJYNlZMVjZLViZlbmNyeXB0ZWRBZElkPUEwODQ4Nzg3MjBPT1gxVkI2SEdVMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    price = price.replace(',', '')
    converted_price = float(price[2:10])

    if(converted_price < 2000):
        send_mail()

    print(converted_price)
    print(price)
    print(title.strip())



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('cycobot1233@gmail.com', 'hazafugtsttplosi')
    subject = 'Price Fell Down!'
    body = 'Check The Amazon Link https://www.amazon.in/Crucial-DDR4-2400-192000-CL17/dp/B019FREJOQ/ref=sr_1_1_sspa?crid=CYXMMJMQ2ZMW&dchild=1&keywords=2400mhz+8gb+ram&qid=1598776359&sprefix=2400mhz+8g%2Caps%2C332&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNExVWlo0SlVEWlJSJmVuY3J5cHRlZElkPUEwMzAxODc5MTlPRDJYNlZMVjZLViZlbmNyeXB0ZWRBZElkPUEwODQ4Nzg3MjBPT1gxVkI2SEdVMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'cycobot1233@gmail.com',
        'kuldeepjain1233@gmail.com',
        msg
    )
    print("Hey E-Mail is Sent")

    server.quit()

while True:
    check_price()
    time.sleep(60 * 60)
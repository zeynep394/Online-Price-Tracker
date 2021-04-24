
import requests #access the url and pull data out of there
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.bershka.com/tr/kadin/gi%CC%87yi%CC%87m/etek/pilili-mini-etek-c1010193224p102739199.html?colorId=250'


headers={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

def price():
    page =requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    #title=soup.find(id="productTitle").get_text()
    price = soup.find(class_='current-price-elem').get_text()
    
    price=price[:-3].replace(",",".")
    print(price)
    convert=float(price)

    starting_price=convert
    if(convert<199.95):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('zeynepderbentt@gmail.com','yasxbsiiolutxvda')

    subject = 'Price Dropped!'

    body =' Check the link https://www.bershka.com/tr/kadin/gi%CC%87yi%CC%87m/etek/pilili-mini-etek-c1010193224p102739199.html?colorId=250'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'zeynepderbentt@gmail.com',
        'zeynepderbent15@gmail.com',
        msg
    )
    print("Mission Completed!")

    server.quit()


while(True):
    price()
    time.sleep(60*60*24)

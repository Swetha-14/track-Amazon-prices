import requests
from bs4 import BeautifulSoup
import smtplib
import time

# URL of your Amazon Product
URL = 'https://www.amazon.in/gp/product/B08Lsdgysgd'

headers = {"User-Agent":'*your user agent id'}
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price < 1.700):
        send_mail()
    print(converted_price)
    print(title.strip())

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(*email, *app password)
        subject = 'Price fell down!'
        body = 'Check the amazon link https://www.amazon.in/gp/product/dsgdjsdh' # URL of your Amazon Product
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            *from email*,
            *to email*,
            msg
        )
        print('Hey! Email has been sent!')
        server.quit()

while(True):
    check_price()
    time.sleep(3600)

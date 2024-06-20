import requests
from bs4 import BeautifulSoup
from threading import Timer

URL = 'https://www.flipkart.com/boat-rockerz-510-super-extra-bass-bluetooth-headset/p/itm80f91d1c64beb?pid=ACCEZB5QGQBDWVWD&lid=LSTACCEZB5QGQBDWVWD3AFNTU&marketplace=FLIPKART&store=0pm%2Ffcn&srno=b_1_34&otracker=browse&fm=organic&iid=e027f2a5-ace0-423f-acb3-c1fb9e12104d.ACCEZB5QGQBDWVWD.SEARCH&ppt=browse&ppn=browse&ssid=jib1auf57k0000001696617520063'

headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

set_price = 1000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_='B_NuCI').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find(class_='_30jeq3 _16Jk6d').get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    print('if the price drops you will get an email :)')
    
    Timer(60, check_price).start()

check_price()
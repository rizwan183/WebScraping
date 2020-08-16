import requests
from bs4 import BeautifulSoup

page = 1
while True:

    url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp3&fm=neo%2Fmerchandising&iid=M_6373d678-a1b6-4d1b-9f5d-9500da9371b6_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=fr08w8v2000000001597405299621&page={page}'.format(page=page)
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find('div', attrs={'id': 'container'})
    print(data)
    for mobile in data.find_all('div', attrs={'class': 'bhgxx2 col-12-12'}):
        try:
            print("Name :", mobile.find('div', attrs={'class': '_3wU53n'}).get_text())
            print("Mobile Specification :", mobile.find('ul', attrs={'class': 'vFw0gD'}).get_text())
            print("Price :", mobile.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).get_text())
        except:
            pass

    page=page+1

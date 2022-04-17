from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Lucknow"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div',class_='mb-srp__card')

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['title', 'carpet_area', 'price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h2', class_="mb-srp__card--title").text.replace('\n', '')
        carpet_area = list.find('div', class_="mb-srp__card__summary--value").text.replace('\n', '')
        price = list.find('div', class_="mb-srp__card__price--amount").text.replace('\n', '')
        
        
        info = [title, carpet_area, price]
        thewriter.writerow(info)


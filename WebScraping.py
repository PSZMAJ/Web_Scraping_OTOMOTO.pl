# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:56:49 2020

@author: Przemek
"""

from bs4 import BeautifulSoup
from requests import get 
import datetime



### ---> In 'url' put the link to offer about cars you like or you search
url = 'https://www.otomoto.pl/osobowe/audi/a8/?search%5Bfilter_enum_generation%5D%5B0%5D=gen-d3-2002-2010&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D='

page = get(url)
bs = BeautifulSoup(page.content, 'html.parser')

### ---> get date, day and hour.
day = datetime.datetime.now().strftime("%B %d, %Y")
hour = datetime.datetime.now().strftime("%I:%M%p")


### ---> function 'get_info()' get information from webside('url') and save to file
def get_info():
    ### ---> save all information on file, file name is today date
    with open (day +'.txt', 'w') as file:  
        print('Downloaded on: ', day, ' hour:', hour, file=file)
        print('*****' * 25, file = file)
        
        
        ### ---> this loop downloads information about car, name, price, location and other.
        for offer in bs.find_all('div', class_='offer-item__content ds-details-container'):
            car_name = offer.find('h2', class_='offer-title ds-title').get_text().strip()
            car_price = offer.find(class_='offer-price__number ds-price-number').get_text().strip()
            car_location = offer.find('span', class_='ds-location-city').get_text().strip()
            car_more_info = offer.find('div',class_='offer-item__title').get_text().strip()
            params = offer.find_all('li', class_ = 'ds-param')
            data = []
            
            
            ### ---> this loop downloads information about year car and other information(mileage,capacity,fule)
            for param in params:
                data.append(param.get_text().strip())
                
            ### ---> this loop downloads a link to offer
            for a in offer.find_all('a', href=True, text=True):
                link_text = a['href']
            
            ### ---> printing information and save on file  
                print('Car name: {}'.format(car_name), file = file)
                print('More information:',car_more_info[10:].strip(), file = file)
                print('Car location: {}'.format(car_location), file = file)
                print('Car year:', data[:1], file = file)
                print('Car mileage:', data[1:2], file = file)
                print('Car capacity:', data[2:3], file = file)
                print('Car fuel:', data[3:], file = file)
                print('Car price: {0} ' 'Cash'.format(car_price), file = file)
                print(link_text, file = file)
                print('', file = file)
                print('*****' * 25, file = file)
    

get_info()




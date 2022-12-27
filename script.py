import requests
from bs4 import BeautifulSoup
from flask import Flask
import re
app = Flask(__name__)

@app.route('/')
def fuel_prices():
    Petrol_Website = "https://www.ndtv.com/fuel-prices/petrol-price-in-all-city"

    PetrolWebsite_response = requests.get(Petrol_Website)
    Petrol_Soup = BeautifulSoup(PetrolWebsite_response.text,'html.parser')
    Petrol_Rows = Petrol_Soup.find('div',{'id':'myID'}).find('tbody').find_all('tr')

    Diesel_Website = "https://www.ndtv.com/fuel-prices/diesel-price-in-india"

    Diesel_Website_response = requests.get(Diesel_Website)
    Diesel_Soup = BeautifulSoup(Diesel_Website_response.text,'html.parser')
    Diesel_Rows = Diesel_Soup.find('div',{'id':'myID'}).find('tbody').find_all('tr')
    data = []
    data2 = []
    for Petrol_Row in Petrol_Rows:
        try:
            cells = Petrol_Row.find_all('td')
            state = cells[0].text
            price = cells[1].text
            price = re.sub(r'[^\d.]+', '', price)  # remove all non-digit characters
            data.append({'City':state,'PetrolPrice': price})
        except IndexError:
            print('Error: Could not extract data from Petrol website')

    for Diesel_Row in Diesel_Rows:
        try:
            cells = Diesel_Row.find_all('td')
            state2 = cells[0].text
            price2 = cells[1].text
            price2 = re.sub(r'[^\d.]+', '', price2)  # remove all non-digit characters
            data2.append({'City':state2,'DieselPrice': price2})
        except IndexError:
            print('Error: Could not extract data from Diesel website')

    combined_data = []
    city_prices = {}

    for item in data:
        city_prices[item['City']] = {'PetrolPrice': item['PetrolPrice']}

    for item in data2:
        city_prices[item['City']]['DieselPrice'] = item['DieselPrice']

    for city, prices in city_prices.items():
        combined_data.append({'City': city, **prices})
        
    return(combined_data)
if __name__ == "__main__":
    app.run()

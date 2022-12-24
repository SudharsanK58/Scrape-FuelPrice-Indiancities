import requests
from bs4 import BeautifulSoup
from flask import Flask
import re
app = Flask(__name__)

@app.route('/AllCityprices')
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
    for Petrol_Row in Petrol_Rows:
        try:
            cells = Petrol_Row.find_all('td')
            state = cells[0].text
            price = cells[1].text
            price = re.sub(r'[^\d.]+', '', price)  # remove all non-digit characters
            data.append({state: [{'Petrol price': price}]})
        except IndexError:
            print('Error: Could not extract data from Petrol website')

    for Diesel_Row in Diesel_Rows:
        try:
            cells = Diesel_Row.find_all('td')
            state2 = cells[0].text
            price2 = cells[1].text
            price2 = re.sub(r'[^\d.]+', '', price2)  # remove all non-digit characters
            data.append({state2: [{'Petrol Price': price,'Diesel price': price2}]})
        except IndexError:
            print('Error: Could not extract data from Diesel website')

    for i in range(699):
        data.pop(0)
        
    return(data)
if __name__ == "__main__":
    app.run()







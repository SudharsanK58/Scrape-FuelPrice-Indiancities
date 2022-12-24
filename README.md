# Fuel Prices Scraper
This code is a web scraper that retrieves fuel prices for petrol and diesel in different cities in India from the websites https://www.ndtv.com/fuel-prices/petrol-price-in-all-city and https://www.ndtv.com/fuel-prices/diesel-price-in-india, respectively.

## Requirements
The following libraries are required to run this code:

- requests
- bs4 (BeautifulSoup)
- flask
- re (regular expression)

Install these libraries by running the following command:

## Copy code

```sh
pip install requests bs4 flask re
```
```sh
python script.py
```
This will start the Flask app, which will run on your local machine at the default port (5000).

To retrieve the fuel prices, send a GET request to the URL http://localhost:5000/AllCityprices. The response will be a list of dictionaries, each containing the name of a city and the petrol and diesel prices in that city.

## Code Overview
The code consists of a single function, fuel_prices, which is decorated with the @app.route decorator. This function is called when the /AllCityprices route is requested.

The function begins by sending a GET request to the website for petrol prices and another GET request to the website for diesel prices. It then uses the BeautifulSoup library to parse the HTML content of the responses and searches for tr elements within a tbody element within a div element with the id attribute set to myID.

For each petrol row and diesel row, the function extracts the data from the cells and stores it in a dictionary. It then removes all non-digit characters from the price data using the re library.

Finally, the function removes the first 699 elements from the data list and returns the remaining list.

## Tips
- If you want to scrape a different website or modify the data that is being scraped, you will need to modify the BeautifulSoup code that searches for the relevant elements and extracts the data.
- If the website you are scraping changes its HTML structure, you may need to update the BeautifulSoup code to ensure that it is still able to find the relevant elements.
- Be mindful of the terms of use and robots.txt file of the website you are scraping. Some websites may prohibit web scraping or have limits on the amount of data that can be accessed. It is generally good practice to request permission before scraping a website.

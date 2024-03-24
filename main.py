import requests, bs4

from functions import *

def main():

    #* Scraping website data

    res = requests.get('https://www.sportsbet.com.au/horse-racing/australia-nz/warrnambool/race-1-8106222')    # URL for the Sportsbet page of the race

    soup = bs4.BeautifulSoup(res.text, "lxml")

    prices = soup.select('.priceText_f71sibe')

    race_name = soup.select('title')[0].getText()

    #* Data manipulation

    prices = list(map(lambda n: n.getText(), prices))    # Get the text from the list of prices soup objects

    while prices[-1] != 'EW':    # Remove the tips on the side of the webpage from the price data (if they exist)
        prices.pop()

    prices = list(filter(lambda n: n != 'EW', prices))    # Remove the 'EW' button from the price data

    prices = list(map(lambda n: float(n), prices))    # Turni prices into type float

    prices = remove_every_second_list_element(prices)    # Keepi only the win prices in the price list (remove the place prices)

    #* Data calculation

    race_percentage = percentage_calculator(prices)

    #* Output

    print(f'{race_name}: {race_percentage - 100:.2f}%')

if __name__ == '__main__':
    main()
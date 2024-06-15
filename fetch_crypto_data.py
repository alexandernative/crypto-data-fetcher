# fetch_crypto_data.py
import requests
import csv

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum',
        'order': 'market_cap_desc',
        'per_page': 2,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()

    with open('crypto_prices.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Cryptocurrency', 'Price (USD)', 'Circulating Supply', 'All Time High (USD)'])
        for coin in data:
            writer.writerow([coin['name'], coin['current_price'], coin['circulating_supply'], coin['ath']])

if __name__ == "__main__":
    fetch_crypto_data()

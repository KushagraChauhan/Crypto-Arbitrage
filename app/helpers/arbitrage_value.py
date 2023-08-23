from http import HTTPStatus
from flask import Blueprint, jsonify
from flasgger import swag_from
import requests
from config import logger
from instance import secret_keys


def arbitrage_value_gen():
        # CoinMarketCap API endpoint for getting the price of BTC on Binance
    CMC_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC"
    # CoinMarketCap API Key
    CMC_API_KEY = secret_keys.CMC_API_KEY

    # Get the current price of BTC on Binance using the CoinMarketCap API
    #cmc_params = {"symbol": "BTC", "convert": "USD", "exchange": "binance"}
    cmc_headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
    cmc_response = requests.get(CMC_URL,headers=cmc_headers).json()
    cmc_price = cmc_response["data"]["BTC"]["quote"]["USD"]["price"]

    try:
        ## bitcoin binance
        binance_url = "https://pro-api.coinmarketcap.com/v1/exchange/assets?id=270"
        binance_respose = requests.get(binance_url,headers=cmc_headers).json()
        binance_price = binance_respose["data"]
        binance_res = []
        for i in binance_price:
            if i["currency"]["symbol"] == "BTC":
                binance_res.append(i["currency"]["price_usd"])
    except(ConnectionError, TimeoutError) as e:
        logger.error("We have a problem, sir %s", e)


    try:
    ## bitcoin kraken
        kraken_url = "https://pro-api.coinmarketcap.com/v1/exchange/assets?id=37"
        kraken_response = requests.get(kraken_url, headers=cmc_headers).json()
        kraken_price = kraken_response["data"]

        kraken_res = []
        for i in kraken_price:
            if i["currency"]["symbol"] == "BTC":
                kraken_res.append(i["currency"]["price_usd"])
    except(ConnectionError, TimeoutError) as e:
        logger.error("We have a problem, sir %s", e)

    arbitrage_value = binance_res[0] - kraken_res[0]
    return arbitrage_value
def isArbitagePossible(threshold):
    arbitrage_value = arbitrage_value_gen()
    if threshold > arbitrage_value:
        return True
    else:
        return False

def arbitagePossible(threshold):
    if isArbitagePossible:
        asset = 'BTC'
        exchanges = ['Binance', 'Kraken']
        profit = arbitrage_value_gen()
        return profit
from flasgger import swag_from
import requests
from config import logger
from instance import secret_keys


def arbitrage_value_gen(exchange):
     # CoinMarketCap API endpoint for getting the price of BTC on Binance
    CMC_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC"
    # CoinMarketCap API Key
    CMC_API_KEY = secret_keys.CMC_API_KEY
    cmc_headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
    
    try:
        # Get the current price of BTC on Binance using the CoinMarketCap API
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
        # Get the current price of BTC on Kraken using the CoinMarketCap API
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

    if exchange == "Binance":
        arbitrage_value = binance_res[0] - kraken_res[0]
    else:
        arbitrage_value = kraken_res[0] - binance_res[0]

    return arbitrage_value

def isArbitagePossible(threshold, exchange):
    arbitrage_value = arbitrage_value_gen(exchange)
    if threshold < arbitrage_value:
        return True
    else:
        return False

def arbitagePossible(exchange):
    if isArbitagePossible:
        profit = arbitrage_value_gen(exchange)
        return profit
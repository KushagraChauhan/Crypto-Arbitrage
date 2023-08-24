from flasgger import swag_from
import requests
from config import logger
from instance import secret_keys

## This is the helper method to generate the arbitrage_value from the CMC APIs
def arbitrage_value_gen(exchange):
    """
    Calculate the arbitrage_value from the CMC APIs.
    
    :param exchange: The name of the exchange from which to perform arbitrage.
    :type exchange: string
    :return: The arbitrage_value which is the difference between the price of the two the exchanges
    :rtype: int or float
    """

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


## This is the helper method that checks whether an arbitrage is possible or not against the given threshold
def isArbitagePossible(threshold, exchange):
    """
    Check whether an arbitrage is possible or not against the given threshold
    
    :param exchange: The name of the exchange from which to perform arbitrage.
    :param threshold: The input given by the user to check
    :type exchange: string
    :type threshold: int or float
    :return: True/False based on the calculations
    :rtype: Boolean or string
    """

    arbitrage_value = arbitrage_value_gen(exchange)
    if threshold < arbitrage_value:
        return True
    else:
        return False

## This is the helper method that returns the profit which is equal to the arbitrage value if arbitrage is possible
def arbitagePossible(exchange):
    """
    Return the profit which is equal to the arbitrage value if arbitrage is possible
    
    :param exchange: The name of the exchange from which to perform arbitrage.
    :type exchange: string
    :return: The amount of profit possible
    :rtype: int or float
    """
    if isArbitagePossible:
        profit = arbitrage_value_gen(exchange)
        return profit
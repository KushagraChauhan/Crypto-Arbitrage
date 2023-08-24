from app.models.trade_model import Trade

## Helper method to save data into the DB
def save_trade(asset, exchanges, profit):
    """
    Save the data into the DB
    
    :param asset: The name of the asset
    :type asset: string
    :param exchanges: The list of the exchanges
    :type exchanges: list
    :param profit: The amount of profit 
    :type profit: int or string
    :return: trade object
    """
    trade = Trade(asset=asset, exchanges=exchanges, profit=profit)
    trade.save()
    return trade

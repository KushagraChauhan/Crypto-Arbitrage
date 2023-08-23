from app.models.trade_model import Trade

## Helper method to save data into the DB
def save_trade(asset, exchanges, profit):
    trade = Trade(asset=asset, exchanges=exchanges, profit=profit)
    trade.save()
    return trade

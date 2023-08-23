from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Api
from config import logger
from app.route.history import bp
from app.helpers.database import save_trade
from app.helpers.arbitrage_value import isArbitagePossible, arbitagePossible
import json

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app)
api = Api(app)

## Register the blueprint for historical data
app.register_blueprint(bp, url_prefix='/history')

## Home page route
@app.route('/home')
def index():
    return render_template('arbitrage.html')

## Socket event - Connect 
## When the home page route is loaded..
@socketio.on('connect')
def on_connect():
    logger.info('Client connected')

## Socket event - disconnect
## When the home page route is closed
@socketio.on('disconnect')
def on_disconnect():
    logger.info('Client disconnected')

## Socket event - set_threshold_bk
## This event corresponds to 'Binance To Kraken' when button with id='binance_to_kraken' is pressed on the home page
@socketio.on('set_threshold_bk')
def adjust_threshold_bk(data, methods=['GET', 'POST']):
    threshold = data
    ## Data is only stored in the DB when an arbitrage opportunity has been found, otherwise it is not stored in the DB
    if isArbitagePossible(threshold, "Binance"):
        asset = 'BTC'
        exchanges = ["Binance", "Kraken"]
        profit = arbitagePossible("Binance")
        trade = save_trade(asset, exchanges, profit)
        logger.info(trade.to_json())
        ## This emits 'arbitrage_opportunity' that corresponds to Success
        socketio.emit('arbitrage_opportunity', {'trade': trade.to_json()}, include_self=True)
    
    else:
        asset = 'BTC'
        exchanges = ["Binance", "Kraken"]
        profit = "No Profit"
        data = {
            "asset": asset,
            "exchanges": exchanges,
            "profit": profit
        }
        trade = json.dumps(data)
        logger.info(trade)
        ## This emits 'no_opportunity' that corresponds to Failure
        socketio.emit('no_opportunity', {'trade': trade}, include_self=True)

## Socket event - set_threshold_bk
## This event corresponds to 'Kraken To Binance' when button with id='kraken_to_binance' is pressed on the home page
@socketio.on('set_threshold_kb')
def adjust_threshold_kb(data, methods=['GET', 'POST']):
    threshold = data
    ## Data is only stored in the DB when an arbitrage opportunity has been found, otherwise it is not stored in the DB
    if isArbitagePossible(threshold, "Kraken"):
        asset = 'BTC'
        exchanges = ["Kraken", "Bitcoin"]
        profit = arbitagePossible("Kraken")
        trade = save_trade(asset, exchanges, profit)
        logger.info(trade.to_json())
        ## This emits 'arbitrage_opportunity' that corresponds to Success
        socketio.emit('arbitrage_opportunity', {'trade': trade.to_json()}, include_self=True)
    
    else:
        asset = 'BTC'
        exchanges = ["Kraken", "Binance"]
        profit = "No Profit"
        data = {
            "asset": asset,
            "exchanges": exchanges,
            "profit": profit
        }
        trade = json.dumps(data)
        logger.info(trade)
        ## This emits 'no_opportunity' that corresponds to Failure
        socketio.emit('no_opportunity', {'trade': trade}, include_self=True)

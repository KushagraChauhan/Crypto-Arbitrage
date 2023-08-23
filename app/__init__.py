from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Api
from config import logger
from app.route.history import bp
from app.database import save_trade
from app.helpers.arbitrage_value import isArbitagePossible, arbitagePossible

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app)
api = Api(app)

app.register_blueprint(bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('arbitrage.html')


@socketio.on('connect')
def on_connect():
    logger.info('Client connected')


@socketio.on('disconnect')
def on_disconnect():
    logger.info('Client disconnected')


@socketio.on('set_threshold_bk')
def adjust_threshold_bk(data, methods=['GET', 'POST']):
    threshold = data
    #logger.info("Send : ",data)
    if isArbitagePossible(threshold, "Binance"):
        asset = 'BTC'
        exchanges = ["Binance", "Kraken"]
        profit = arbitagePossible("Binance")
        trade = save_trade(asset, exchanges, profit)
        logger.info(trade.to_json())
        socketio.emit('arbitrage_opportunity', {'trade': trade.to_json()}, include_self=True)

@socketio.on('set_threshold_kb')
def adjust_threshold_kb(data, methods=['GET', 'POST']):
    threshold = data
    #logger.info("Send : ",data)
    if isArbitagePossible(threshold, "Kraken"):
        asset = 'BTC'
        exchanges = ["Kraken", "Bitcoin"]
        profit = arbitagePossible("Kraken")
        trade = save_trade(asset, exchanges, profit)
        logger.info(trade.to_json())
        socketio.emit('arbitrage_opportunity', {'trade': trade.to_json()}, include_self=True)

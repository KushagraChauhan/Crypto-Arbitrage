from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Api
import config
from app.route.arbitrage import bp
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
    print('Client connected')


@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')


@socketio.on('set_threshold')
def adjust_threshold(data, methods=['GET', 'POST']):
    threshold = data
    print("Send : ",data)
    if isArbitagePossible(threshold):
        asset = 'BTC'
        exchanges = ["Binance", "Kraken"]
        profit = arbitagePossible(threshold)
        trade = save_trade(asset, exchanges, profit)
        print(trade.to_json())
        socketio.emit('arbitrage_opportunity', {'trade': trade.to_json()}, include_self=True)

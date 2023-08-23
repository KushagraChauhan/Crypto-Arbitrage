from flask import request, jsonify, Blueprint
from app.models.trade_model import Trade
from app.utils import requires_auth

bp = Blueprint('api', __name__)

@bp.route('/api/trades', methods=['GET'])
@requires_auth
def get_trades():
    trades = Trade.objects.all()
    return jsonify([trade.to_dict() for trade in trades])

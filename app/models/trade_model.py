from datetime import datetime
from mongoengine import Document, ListField, StringField, FloatField, DateTimeField
class Trade(Document):
    asset = StringField()
    exchanges = ListField()
    profit = FloatField()
    timestamp = DateTimeField(default=datetime.utcnow)
    def to_dict(self):
        trade_dict = {
            "asset": self.asset,
            "exchanges": self.exchanges,
            "profit": self.profit,
            "timestamp": self.timestamp
        }
        return trade_dict

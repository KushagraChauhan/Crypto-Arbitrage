from datetime import datetime
from mongoengine import Document, ListField, StringField, FloatField, DateTimeField

## Model for the DB
class Trade(Document):
    """
    Model for the DB
    
    :param Document: Document is likely referring to a class or base class that represents a document in a MongoDB database using an Object-Document Mapping (ODM) framework.  
    """
    asset = StringField()
    exchanges = ListField()
    profit = FloatField()
    timestamp = DateTimeField(default=datetime.utcnow)

    ## Helper method to return a dict from the data
    def to_dict(self):
        trade_dict = {
            "asset": self.asset,
            "exchanges": self.exchanges,
            "profit": self.profit,
            "timestamp": self.timestamp
        }
        return trade_dict

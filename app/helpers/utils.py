from functools import wraps
from flask import request, g, abort

def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == 'kushagra' and auth.password == 'algotest'):
            abort(401)
        return func(*args, **kwargs)
    return decorated

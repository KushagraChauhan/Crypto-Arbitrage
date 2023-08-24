from functools import wraps
from flask import request, g, abort

## Helper method to incorporate basic auth in the history REST API
def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization

        ## This is the username and password for the basic auth
        if not auth or not (auth.username == 'kushagra' and auth.password == 'algotest'):
            abort(401)
        return func(*args, **kwargs)
    return decorated

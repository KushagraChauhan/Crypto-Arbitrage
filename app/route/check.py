from flask import render_template
from app import app

## We can ignore this app route, this is one of the earlier trial/errors
@app.route('/check')
def index():
    return render_template('index.html')

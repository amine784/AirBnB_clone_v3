#!/usr/bin/python3
'''first step to create rest api'''
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exep):
    '''close session'''
    storage.close()
if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST')
    PORT = getenv('HBNB_API_PORT')
    app.run(host=HOST, port=PORT, threaded=True)

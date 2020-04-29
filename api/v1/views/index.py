#!/usr/bin/python3
'''create api'''
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def get_status():
    '''get status route'''
    return(jsonify({"status": "OK"}))

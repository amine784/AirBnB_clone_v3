#!/usr/bin/python3
'''create api'''
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def get_status():
    '''get status route'''
    return(jsonify({"status": "OK"}))


@app_views.route('/stats')
def stat():
    '''get  nbre of all instance'''
    dic = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return(jsonify(dic))

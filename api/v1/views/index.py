#!/usr/bin/python3
"""File that returns more view functions"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """Returns status of object"""
    return jsoniy({'status': 'OK'})


@app_views.route("/api/v1/stats", methods=['GET'], strict_slashes=False)
def get_stats():
    """Returns number of objects by type"""
    return jsonify({
       'amenities': storage.count('Amenity'),
       'cities': storage.count('City'),
       'places': storage.count('Place'),
       'review': storage.count('Review'),
       'states': storage.count('State'),
       'users': storage.count('User')
       })

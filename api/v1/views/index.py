#!/usr/bin/python3
"""File that returns more view functions"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

@app_views.route("/status")
def status():
    """Returns status of object"""
    return jsoniy({'status': 'OK'})

@app_views.route("/api/v1/stats")
def get_stats():
    """Returns number objects by type"""
   return jsonify({
       'amenities': storage.count('Amenity'),
       'cities': storage.count('City'),
       'places': storage.count('Place'),
       'review': storage.count('Review'),
       'states': storage.count('State'),
       'users': storage.count('User')
       })

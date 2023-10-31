#!/usr/bin/python3
"""File containing view functions"""
from flask import Flask, Blueprint, jsonify
from models import storage
import os, json
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down():
    """Closes storage from models"""
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    """Returns 404 error when page not found"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)

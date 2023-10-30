#!/usr/bin/python3
"""File containing view functions"""
from flask import Flask, Blueprint, render_template
from models import FileStorage
import os, json
from api.v1.views import app_views


app = Flask(__name__)
app_views = Blueprint('app_views', __name__)
app.register_blueprint('app_views')

@app.teardown_appcontext
def storage_close():
    """Closes storage from models"""
    return models.storage.close()

@app.route("/states", methods=["GET"])
def get_states():
    """Returns json form of states"""
    return jsonify({"states": states})

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)

#!/usr/bin/python3
"""View for State objects handles restful api actions"""
from api.v1.views import app_views
from models import storage
from flask import jsonify
from flask import abort
from flask import request


@app_views.route('/states', methods=["GET"], strict_slashes=False)
def get_states():
    """Returns list of all state objects"""
    states = storage.all('State')
    states_list = []
    for state in states.values():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/int:<state_id>', methods=["GET"],
                 strict_slashes=False)
def get_state(state_id):
    """Returns specific state of given state id"""
    for state in states:
        if state.get('id') == state_id:
            return jsonify(states)
    return jsonify({"message": "The state you are looking for does not exist"})


if __name__ == "__main__":
    app.run()

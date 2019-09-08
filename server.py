#!/usr/bin/env python3

from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')

@app.route("/", methods=['GET'])
def json_api():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        return jsonify(lista)

if __name__ == "__main__":
    # when using docker, it is important to define host and port
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
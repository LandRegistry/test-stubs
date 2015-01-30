#!/usr/bin/env python
import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

tempstr = '';

@app.route('/set_ppi', methods=['POST'])
def set_tasks():
    global tempstr
    tempstr = request.data
    return request.data

@app.route('/get_ppi', methods=['POST'])
def get_tasks():
    return tempstr


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#!/usr/bin/env python
import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

tempstr = '';

@app.route('/set_ppi', methods=['POST'])
def set_tasks():

    global tempstr

    ppi_amount = request.form['ppi_amount']
    ppi_date = request.form['ppi_date']

    message = '{ "head": { "vars": [ "amount" , "date" , "property_type" ] } , "results": { "bindings": [ { "amount": { "datatype": "http://www.w3.org/2001/XMLSchema#integer" , "type": "typed-literal" , "value": "' + ppi_amount + '" } , "date": { "datatype": "http://www.w3.org/2001/XMLSchema#date" , "type": "typed-literal" , "value": "' + ppi_date + '" } , "property_type": { "type": "uri" , "value": "http://landregistry.data.gov.uk/def/common/terraced" } } ] } }'

    tempstr = message
    return message

@app.route('/get_ppi', methods=['POST'])
def get_tasks():
    return tempstr


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

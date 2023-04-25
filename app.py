#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flasgger import Swagger

from utils import helpers, service

app = Flask(__name__)

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = 'Dynatrace Backend Internship Task 2023'
swagger_config['description'] = 'API for retrieving exchange rates from the National Bank of Poland'
swagger_config['openapi'] = '3.0.5'
swagger_config['specs_route'] = '/'
app.config['SWAGGER'] = swagger_config
Swagger(app, template_file='openapi.yml')


@app.route('/average_exchange_rate')
def average_exchange_rate():
    date = request.args.get('date')
    currency_code = request.args.get('currency_code')

    try:
        helpers.validate_date(date)
        helpers.validate_currency(currency_code)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    result = service.get_average_exchange_rate(currency_code, date)

    return jsonify(result["msg"]), result["code"]


@app.route('/max_min_average')
def max_min_average():
    count = request.args.get('count', default=1, type=int)
    currency_code = request.args.get('currency_code')

    try:
        helpers.validate_count(count)
        helpers.validate_currency(currency_code)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    result = service.get_max_min_average(currency_code, count)

    return jsonify(result["msg"]), result["code"]


@app.route('/major_difference')
def major_difference():
    count = request.args.get('count', default=1, type=int)
    currency_code = request.args.get('currency_code')

    try:
        helpers.validate_count(count)
        helpers.validate_currency(currency_code)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    result = service.get_major_difference(currency_code, count)

    return jsonify(result["msg"]), result["code"]


if __name__ == '__main__':
    app.run(debug=True)

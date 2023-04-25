import requests


NBP_API_URL = "http://api.nbp.pl/api"


def get_average_exchange_rate(currency_code, date) -> dict:
    url = f'{NBP_API_URL}/exchangerates/rates/a/{currency_code}/{date}/?format=json'
    response = requests.get(url)

    if response.status_code == 404:
        return {'msg': {'error': 'no data found for the given date and currency code'},
                'code': 404}

    if response.status_code != 200:
        return {'msg': {'error': 'unknown error from source'},
                'code': response.status_code}

    return {'msg': {'rate': response.json()['rates'][0]['mid']},
            'code': 200}


def get_max_min_average(currency_code, count) -> dict:
    url = f'{NBP_API_URL}/exchangerates/rates/a/{currency_code}/last/{count}/?format=json'
    response = requests.get(url)

    if response.status_code == 404:
        return {'msg': {'error': 'no data found for the given currency code and count'},
                'code': 404}

    if response.status_code != 200:
        return {'msg': {'error': 'unknown error'},
                'code': response.status_code}

    rates = [r['mid'] for r in response.json()['rates']]

    return {'msg': {'min_rate': min(rates), 'max_rate': max(rates)},
            'code': 200}


def get_major_difference(currency_code, count) -> dict:

    url = f'{NBP_API_URL}/exchangerates/rates/c/{currency_code}/last/{count}/?format=json'
    response = requests.get(url)

    if response.status_code == 404:
        return {"msg": {'error': 'no data found for the given currency code and count'},
                "code": 404}

    if response.status_code != 200:
        return {"msg": {'error': "unknown error"},
                "code": response.status_code}

    differences = [r['ask'] - r['bid'] for r in response.json()['rates']]

    return {"msg": {"major_difference": max(differences)},
            "code": 200}

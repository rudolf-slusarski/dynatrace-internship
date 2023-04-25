# Recruitment task for Dynatrace Internship 2023: Flask server for NBP API

## Usage

* First, install the dependencies with ```pip install -r requirements.txt```
* Run the server with ```python3 app.py```
* As per Flask default, debug mode is on. To run the server without it, use ```flask run```
* Further api specification will be available under ```http://localhost:5000/```
* Run the unit tests with ```pytest```

Example queries for the required operations:

1. ```curl http://localhost:5000/average_exchange_rate?currency_code=GBP&date=2023-01-02```
2. ```curl http://localhost:5000/max_min_average?currency_code=USD&count=20```
3. ```curl http://localhost:5000/major_difference?currency_code=EUR&count=30```

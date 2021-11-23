# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime, timedelta

from lib.utility import Executor

"""
1. Capture the related API endpoint
2. Send a request using this API endpoint with your preferred language
3. Test the request response status is whether successful or not
4. Extract the relative humidity (e.g. 60 - 85%) for the day after
tomorrow from the API response (e.g. if today is Monday, then extract the relative humidity for Wednesday)
"""

def setup_function():
    pass

def test_task2():
    # Get current timestamp
    current_datetime = datetime.now()

    # Send api request
    api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc"
    response = Executor.execute(requests.get, api_url)

    # Check response status code is 200
    assert response.status_code == 200

    # Transfer to json
    json_data = json.loads(response.text)

    dayAfterTomorrow = current_datetime + timedelta(days=2)
    dayAfterTomorrow_string = dayAfterTomorrow.strftime("%Y%m%d")
    
    for each_data in json_data["weatherForecast"]:
        if each_data["forecastDate"] == dayAfterTomorrow_string:
            assert each_data["forecastMaxrh"] != None
            assert each_data["forecastMinrh"] != None 

def teardown_function():
    pass
import os
import requests
import json
from pytz import timezone as tz
from datetime import datetime as dt
from pprint import pprint as pp

HOST = 'https://iot33.cumulocity.com'
USER = 'k.oshita@ntt.com'
PASS = 'Qwerty1234'

def get_device_state(device_id):
    headers = {
         "Content-Type": "application/vnd.com.nsn.cumulocity.measurement+json;"
                         "charset=UTF-8;"
                         "ver=0.9",
    }
    response = requests.get(
         HOST + '/measurement/measurements?source=' + device_id,
         headers=headers,
         auth=(USER, PASS),
    )
    data = json.loads(response.text)

    latest_data= data["measurements"][-1]

    print latest_data
    latest_state = latest_data["power"]["power"]["value"]

    return latest_state

#get_device_state('18687')

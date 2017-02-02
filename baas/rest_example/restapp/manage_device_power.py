import os
import requests
import json
from pytz import timezone as tz
from datetime import datetime as dt
from pprint import pprint as pp

HOST = 'https://iot33.cumulocity.com'
USER = 'k.oshita@ntt.com'
PASS = 'Qwerty1234'
DEVICE_ID = '22531'

def set_power(pwr):
    headers = {
      "Content-Type": "application/vnd.com.nsn.cumulocity.measurement+json;"
                    "charset=UTF-8;"
                    "ver=0.9",
      "Accept": "application/vnd.com.nsn.cumulocity.measurement+json;"
              "charset=UTF-8;"
              "ver=0.9",
    }
    body = {
      "source": { "id": DEVICE_ID }, # todo: get source id from api
      "type": "c8y_Linux", # todo: get type from api
      "time": dt.now(tz('UTC')).isoformat(),
      "power": {
        "power": { "value": pwr, "unit": "on/off" },
      },
    }

    print body
    response = requests.post(
        HOST + '/measurement/measurements',
        headers=headers,
        data=json.dumps(body),
        auth=(USER, PASS),
    )
    print response.text
    return response

def power_on_device(device_id):
    # TODO real things_cloud methods
    set_power(1)
    return True

def power_off_device(device_id):
    # TODO real things_cloud methods
    set_power(0)
    return True

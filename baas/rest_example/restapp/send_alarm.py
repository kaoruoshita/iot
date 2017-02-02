import os
import requests
import json
from pytz import timezone as tz
from datetime import datetime as dt
from pprint import pprint as pp
from time import sleep
from daemon import runner
from device_state import get_device_state

HOST = 'https://iot33.cumulocity.com'
USER = 'k.oshita@ntt.com'
PASS = 'Qwerty1234'
DEVICE_ID = '22531'

def set_alarm():
    state = get_device_state(DEVICE_ID)
    print state
    if state == 0:
         print "Will send alarm"
   	 headers = {
    		 "Content-Type": "application/vnd.com.nsn.cumulocity.alarm+json;"
                	         "charset=UTF-8;"
                                 "ver=0.9",
         }
 	 body = {
   		 "source": { "id": DEVICE_ID }, # todo: get source id from api
   		 "type": "c8y_Linux", # todo: get type from api
   		 "time": dt.now(tz('UTC')).isoformat(),
   	         "status" : "ACTIVE",
                 "severity" : "MAJOR",
                 "text" :  'Device is powered Off',
         }
 	 response = requests.post(
   		 HOST + '/alarm/alarms',
   		 headers=headers,
	         data=json.dumps(body),
                 auth=(USER, PASS),
         )
 	 return response

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            set_alarm()
            sleep(5)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()

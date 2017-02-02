import requests
import json
import picamera
from time import sleep

HOST = 'https://iot33.cumulocity.com'
USER = 'k.oshita@ntt.com'
PASS = 'Qwerty1234'


def clean_up_binaries():
   response = requests.get(
      HOST + '/inventory/binaries',
      auth=(USER, PASS),
   )
   data =  json.loads(response.text)
   resources = data["managedObjects"]
   for image in resources:
      binaryId = image["id"]
      response = requests.delete(
         HOST + '/inventory/binaries/' + binaryId,
         auth=(USER, PASS),
      )
      print response

def take_photo():
   
   camera = picamera.PiCamera()
   file_name = 'power.jpg'
   camera.capture(file_name)
   return (file_name)

def send_to_tc(file_name):
  image = open(file_name, 'rb')
  files = {
    'object': ("", '{"name": "power", "type": "image/png"}'),
    'file': (file_name, image, 'image/png'),
  }
  response = requests.post(
    HOST + '/inventory/binaries',
    files=files,
    auth=(USER, PASS),
  )
  print response
  return response


count = 0
while (count < 1):
   print 'The count is:', count
   #clean_up_binaries()
   file_name = take_photo()

   sleep(5)
   send_to_tc(file_name)
   count = count + 1

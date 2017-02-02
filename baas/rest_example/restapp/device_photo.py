import requests
import json

HOST = 'https://iot33.cumulocity.com'
USER = 'k.oshita@ntt.com'
PASS = 'Qwerty1234'


def get_latest_photo():
   response = requests.get(
      HOST + '/inventory/binaries',
      auth=(USER, PASS),
   )
   data =  json.loads(response.text)
   resources = data["managedObjects"]

   latest_image = {}
   latest_binaryId = ''
   for image in resources:
      updated_at = image["lastUpdated"]
      if latest_image:
          if latest_image["lastUpdated"] < updated_at:
              latest_image = image
              latest_binaryId = image["id"]
      else:
          latest_image = image   
   print "latest ID??"
   print latest_binaryId
   response = requests.get(
      HOST + '/inventory/binaries/' + latest_binaryId,
      auth=(USER, PASS),
   )
   image_name = '/home/kaoru.oshita/rest_example/restapp/power_photo.jpg'
   with open(image_name, 'wb') as f:
        for chunk in response.iter_content():
            f.write(chunk)


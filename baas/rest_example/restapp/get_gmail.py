import requests
from requests.auth import HTTPBasicAuth
import json
import base64

client_id = '22805444837-umlkhnc8507v9ooggel996vcnpgfnhbq.apps.googleusercontent.com'
client_secret = 'lUcbKIaN7elNXNuffaDoWAUu'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'https://www.googleapis.com/auth/gmail.readonly'
grant_type = 'authorization_code'
code = '4/F1r39wrFmn_OMfa2W3wrMGmeQz9YCLVmg_AzFvcXbAk'
refresh_token = '1/IpfjmZ3eEsk4ki3LuQl8qorN1F17ZeOcq9eLKRVrLgM'
data = "client_id=22805444837-umlkhnc8507v9ooggel996vcnpgfnhbq.apps.googleusercontent.com&client_secret=lUcbKIaN7elNXNuffaDoWAUu&refresh_token=1/IpfjmZ3eEsk4ki3LuQl8qorN1F17ZeOcq9eLKRVrLgM&grant_type=refresh_token"

import subprocess

#token = 'Bearer ya29.GlzlA5uxRRHjS4HB6-K7v63wpo3Fkzje-G1pFla3gc5dkPsH0V0cGYImv434D2s9eP1Ts0DqBikp6dc12TW21K3bh-HSAF8-kQunfNxLEPreOYONKJQtbKdB6ZyPAQ'
#headers = {'Authorization': token}
def refresh_token():
    url = 'https://accounts.google.com/o/oauth2/token'
    response = requests.post(url,
                             data = {'client_id': '22805444837-umlkhnc8507v9ooggel996vcnpgfnhbq.apps.googleusercontent.com',
                                      'client_secret': 'lUcbKIaN7elNXNuffaDoWAUu',
                                      'refresh_token': '1/IpfjmZ3eEsk4ki3LuQl8qorN1F17ZeOcq9eLKRVrLgM',
                                      'grant_type': 'refresh_token',
                                     
                                    }
                            )
    data = json.loads(response.text)
    return 'Bearer ' + data['access_token']

def get_message_details(message_id, token):
    url = 'https://www.googleapis.com/gmail/v1/users/me/messages/' + message_id
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers, verify=False)
    data = json.loads(response.text)

    message_headers = data['payload']['headers']
    
    from_address = ''
    date = ''
    subject = ''

    for h in message_headers:
        if h['name'] == 'From':
            from_address = h['value']
        if h['name'] == 'Date':
            date = h['value']
        if h['name'] == 'Subject':
            subject = h['value']
    
    return (from_address, date, subject)

def get_emails():
    url = 'https://www.googleapis.com/gmail/v1/users/me/messages/'
    token = refresh_token()
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers, verify=False)
    print response.text
    messages = json.loads(response.text)['messages']

    result = []
    for m in messages:
        message_id = m['id']
        (from_address, date, subject) = get_message_details(message_id, token)
        result.append({
           'from_address': from_address,
           'date' : date,
           'subject' : subject
        }) 
    return result


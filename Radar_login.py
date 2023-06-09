#! /usr/bin/python

import requests
import json


radarendpointurl = 'https://radar.wandera.com'
radarusername = #'write_here_your_username'
radarpassword = #'write_here_your_username_password'
childaccountid = #'write_here_your_radar_portalid'

# do not modify the below

def loadradar():
    print('Attempting to login to Radar with ' + radarusername + ' user.')
    loadcredentialsurl = radarendpointurl + '/auth/v4/getToken'
    payload = {
                'username': radarusername,
                'password': radarpassword,
                'sessionId': '28ece5078288ab76867b26244ebd4a39', #random number
                'remember': 'true', #needed
                'totp': '', #needed
                'backupCode': '' #needed
            }
   
    try:
        r = requests.post(loadcredentialsurl, json=payload)

    except:
        print('Error logging into Radar API - exception')
        os._exit(1)

    if (r.text.startswith('{"code"')):
        print('Error logging into Radar API - code' + r.text)
        os._exit(1)
    
    responsejson = json.loads(r.text)
    token = (responsejson['token'])
    global radartoken           #this token will be used for all API requests
    radartoken = 'Bearer ' + token
    print('Your Radar token for further API scraping is:\n' +radartoken)


if __name__ == "__main__":
    loadradar()

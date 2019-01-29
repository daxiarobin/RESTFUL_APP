

import requests
from requests.auth import HTTPBasicAuth
import json

sdnserver = "10.59.13.71"
sdnport = "12443"
baseurl = "com.oiforum.json"
targetobj = "ndm/network/1/endpoint/352723062886"
url = "https://" + sdnserver + ":" + sdnport + "/" \
    + baseurl + "/" + targetobj

username = "administrator"
password = "KOR1ant+"


myResponse = requests.get(url,auth=HTTPBasicAuth(username,password),verify=False)
if(myResponse.ok):
    jData = json.loads(myResponse.content)
    print ("The response contains {0} properties".format(len(jData)))
    print ("\n")
    '''
    for key in jData:
        print (str(key) + " : " + str(jData[key]) + "\n")
    else:
        myResponse.raise_for_status()
    '''
    print (json.dumps(jData,sort_keys=True,indent=4))
    

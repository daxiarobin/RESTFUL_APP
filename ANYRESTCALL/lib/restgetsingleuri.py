'''
Purpose: REST GET opration against a single uri
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-28 v1.0 YS Create the 1st version
'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth
import json
import re
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class restGetSingleUri(object):
    def __init__(self,securemode,username,password,sslverification,logfo,verbose):
        self.securemode = securemode
        self.username = username
        self.password = password
        self.sslverification = sslverification
        self.logfo = logfo
        self.verbose = verbose
        self.fulluri = ""
        
    def restGetOperation(self,fulluri):
        self.fulluri = fulluri
        tmpstr = "REST GET Started: "+fulluri
        self.writeLog(self.logfo,tmpstr)
        print (tmpstr)
        if re.match('yes',self.securemode,flags=re.I):
            myResponse = requests.get(self.fulluri,\
                                      auth=HTTPBasicAuth(self.username,self.password),\
                                      verify=self.sslverification)
        else:
            myResponse = requests.get(self.fulluri,verify=self.sslverification)
        
        if (myResponse.ok):
            jData = json.loads(myResponse.content)
            tmpstr = "REST GET OK: "+fulluri
            self.writeLog(self.logfo,tmpstr)
            self.writeLogNotime(self.logfo,json.dumps(jData,sort_keys=True,indent=4))
        else:
            jData = None
            tmpstr = "REST GET Failed: "+fulluri
            self.writeLog(self.logfo,tmpstr)
        print (tmpstr)
        if re.match('yes',self.verbose, flags=re.I):
            print (json.dumps(jData,sort_keys=True,indent=4))
        return jData
    
    def getTimestamp(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp
    
    def writeLog(self,fo,str):
        currenttime = self.getTimestamp()
        fo.write(currenttime+' '+str+'\n')
        return
    
    def writeLogNotime(self,fo,str):
        fo.write(str+'\n')
        return
        
            
        
        


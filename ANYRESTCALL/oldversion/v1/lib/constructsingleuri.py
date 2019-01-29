'''
Purpose: construct the single uri link based on the input
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-28 v1.0 YS Create the 1st version
'''

import re

class constructSingleuri(object):
    def __init__(self,server,port,httphead):
        self.server = server
        self.uri = ""
        self.port = port
        self.httphead = httphead
        self.fulluri = ""
        
    def createfulluri(self,uri):
        self.uri = uri
        
        '''
        add "/" ahead of the uri if it is not there
        eg: 
          if the user input is ndm/network/1
          then it will be changed to /ndm/network/1
        '''
        if not re.match(r'\/',self.uri[0]):
            self.uri = "/" + self.uri
        self.fulluri = self.httphead + self.server + ":" +\
            str(self.port) + self.uri
        
        return self.fulluri
        
        

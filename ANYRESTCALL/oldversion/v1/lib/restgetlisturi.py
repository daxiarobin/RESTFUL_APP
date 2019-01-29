'''
Purpose: REST GET opration against uri list
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-28 v1.0 YS Create the 1st version
'''

from restgetsingleuri import resetGetSingleUri

class restGetListUri(object):
    def __init__(self,securemode,username,password,sslverification,logfo,fullurilist):
        self.securemode = securemode
        self.username = username
        self.password = password
        self.sslverification = sslverification
        self.logfo = logfo
        self.fullurilist = fullurilist
        self.restsingleuri = resetGetSingleUri(securemode,username,password,\
                                               sslverification,logfo)
        
    def restGetOperation(self):
        for fulluri in self.fullurilist:
            jData = self.restsingleuri.restGetOpreation(fulluri)
            
'''
Purpose: REST GET opration against uri list
Author: Yifeng Shen
Version: 1.1
Change History:
2019-01-28 v1.0 YS Create the 1st version
2019-01-30 v1.1 YS Add version option
'''

from restgetsingleuri import restGetSingleUri

class restGetListUri(object):
    def __init__(self,securemode,username,password,sslverification,logfo,fullurilist,verbose):
        self.securemode = securemode
        self.username = username
        self.password = password
        self.sslverification = sslverification
        self.logfo = logfo
        self.fullurilist = fullurilist
        self.verbose = verbose
        self.restsingleuri = restGetSingleUri(securemode,username,password,\
                                               sslverification,logfo,self.verbose)
        self.jDataList = []
    def restGetOperation(self):
        for fulluri in self.fullurilist:
            jData = self.restsingleuri.restGetOperation(fulluri)
            self.jDataList.append(jData)
            
        return self.jDataList
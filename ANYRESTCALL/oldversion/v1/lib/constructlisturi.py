'''
Purpose: construct the full uri list 
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-28 v1.0 YS Create the 1st version
'''

from constructsingleuri import constructSingleuri

class constructListuri(object):
    def __init__(self,server,port,urilist,httphead):
        self.server = server
        self.port = port
        self.urilist = urilist
        self.httphead = httphead
        self.fullurilist = []
        self.constructsingleuri = constructSingleuri(server,port,httphead)
        
    def createfullurilistGet(self):
        '''
        The uri list create here will be used for REST GET operation
        '''
        for uri in self.urilist:
            fulluri = self.constructsingleuri.createfulluri(uri)
            self.fullurilist.append(str(fulluri))
        return self.fullurilist
    
    def createfullurilistPost(self):
        '''
    The uri list create here will be used for REST POST operation
        TO BE IMPLEMENT
        '''
        return self.fullurilist
        
'''
Purpose: execute any REST GET operation
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-24 v1.0 YS Create the 1st version
'''

import sys,getopt,os,re
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), './lib/'))
if libpath not in sys.path:
    sys.path.append(libpath)
from usage import UsAge
from endprogramm import EndProgramm
from constructlisturi import constructListuri
from restgetlisturi import restGetListUri
from restpostlisturi import restPostListUri
    
def main(argv):
    version = '1.0'
    programmname = 'restcall'
    logfo = None
    endprogramm = EndProgramm()
    usage = UsAge(argv,version,programmname)
    result,securemode,httphead,server,port,urilist,opttype,username,\
        password,outputdic,logfilepath,sslverification = usage.readInput()
 
    if result > 0:
        endprogramm.terminate(result,logfo)    
    try:
        logfo = open(logfilepath,'a')
    except Exception:
        result = 12
        endprogramm.terminate(result,logfo)
       
    constructlisturi = constructListuri(server,port,urilist,httphead)
    
    if re.match('get',opttype):
        fullurilist = constructlisturi.createfullurilistGet()
        restgetlisturi = restGetListUri(securemode,username,password,\
                                    sslverification,logfo,fullurilist)
        restgetlisturi.restGetOperation()
    else:
        fullurilist = constructlisturi.createfullurilistPost()
        restpostlisturi = restPostListUri(securemode,username,password,\
                                    sslverification,logfo,fullurilist)
        restpostlisturi.restPostOperation()
    
    
    endprogramm.terminate(result,logfo)

if __name__ == "__main__":
    main(sys.argv[1:])
    
    


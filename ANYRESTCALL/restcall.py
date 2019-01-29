'''
Purpose: execute any RESTFUL operation (get and post)
Author: Yifeng Shen
Version: 2.0
Change History:
2019-01-24 v1.0 YS Create the 1st version
2019-01-29 v2.0 YS Use getopts class instead of usage class to 
                   read input arguments
'''

import sys,os,re
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), './lib/'))
if libpath not in sys.path:
    sys.path.append(libpath)
from getopts import GetOpts
from inputopts import InputOpts
from endprogramm import EndProgramm
from constructlisturi import constructListuri
from restgetlisturi import restGetListUri
from restpostlisturi import restPostListUri
from validateopts import validateOpts
    
def main():
    version = '2.0'
    programmname = 'restcall'
    logfo = None
    endprogramm = EndProgramm()
  
    '''
    Build new option list
    '''
    optlist_add = []
    optlist_del = []
    
    '''
    Get input values
    '''
    opts = GetOpts(version,programmname,optlist_add,optlist_del)
    if opts.result != 0:
        endprogramm.terminate(opts.result,logfo)
        
    '''
    validate the input args
    '''
    validateopts = validateOpts(opts)
    result,opts,urilist,httphead,logfilepath = validateopts.createInput()    

    if result > 0:
        endprogramm.terminate(result,logfo)
        
    try:
        logfo = open(logfilepath,'a')
    except Exception:
        result = 12
        endprogramm.terminate(result,logfo)
       
    constructlisturi = constructListuri(opts.args.server,\
                                        opts.args.port,urilist,httphead)
    
    if re.match('get',opts.args.type):
        fullurilist = constructlisturi.createfullurilistGet()
        restgetlisturi = \
            restGetListUri(opts.args.mode,opts.args.user,\
                           opts.args.password,\
                                    opts.args.verify,logfo,fullurilist,\
                                    opts.args.verbose)
        restgetlisturi.restGetOperation()
    elif re.match('post',opts.args.type):
        fullurilist = constructlisturi.createfullurilistPost()
        restpostlisturi = restPostListUri(opts.args.mode,opts.args.user,\
                           opts.args.password,\
                                    opts.args.verify,logfo,fullurilist,\
                                    opts.args.verbose)
        restpostlisturi.restPostOperation()
    
    
    endprogramm.terminate(result,logfo)
    
if __name__ == "__main__":
    main()
    
    


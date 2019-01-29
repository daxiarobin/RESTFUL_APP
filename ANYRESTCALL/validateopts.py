'''
Purpose: validate the input args
Author: Yifeng Shen
Version: 1.0
Change History:
2019-01-29 v1.0 YS Create the 1st version
'''

import os,sys,re
import getpass
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), './lib/'))
if libpath not in sys.path:
    sys.path.append(libpath)

class validateOpts(object):
    '''
    :param - opts (object of GetOpts)
    
    :return - result: an integer value indicate whether there is error
              opts: the object with the updated input values
              urilist: internal list contains uri(s)
              logfilepath: full path of the log file
              httphead: either "https://" or "http://" based on secure mode
              
    '''
    
    def __init__(self,opts):
        self.opts = opts
        self.result = 0
        
        
    def createInput(self):
        
        '''
        set default values
        '''
        if not bool(self.opts.args.port):
            self.opts.args.port = '12443'
        
        if not bool(self.opts.args.mode):
            self.opts.args.mode = 'yes'
        
        if not bool(self.opts.args.output):
            self.opts.args.output = \
                os.path.abspath(os.path.join(os.path.dirname(__file__), './output'))
        
        if not bool(self.opts.args.type):
            self.opts.args.type = 'get'
        
        if not bool(self.opts.args.log):
            self.opts.args.log = 'results.log'
            
        if not bool(self.opts.args.verify):
            self.opts.args.verify = False
        
        '''
        addtional return values
        '''
        self.urilist = []
        self.httphead = 'https://'
        self.logfilepath = ''
        
        
        self.validation()
        return self.result,self.opts,self.urilist,self.httphead,self.logfilepath
    
    def validation(self):
        '''
        This function is used to validate all the user input
        '''
        
        '''
        check whether the server address is provided or not
        '''
        if not bool(self.opts.args.server):
            self.result = 4
            self.opts.printUsage()
            return
        
        '''
        check whether the server port is availabe or not
        '''
        if not bool(self.opts.args.port):
            self.result = 5
            return
        
        '''
        uri or uri list file must be specified
        '''
        if not bool(self.opts.args.uri) and not bool(self.opts.args.file):
            self.result = 6
            self.opts.printUsage()
            return 
    
        if bool(self.opts.args.uri):
            self.urilist.append(elf.opts.args.uri.rstrip())
            
        if bool(self.opts.args.file):
            if not os.path.isfile(self.opts.args.file):
                self.result = 7
                return
            else:
                try:
                    fo = open(self.opts.args.file,'r')
                    for line in fo:
                        self.urilist.append(line.rstrip())
                except Exception:
                    self.result = 9
                    return
        
        '''
        verify the output directory
        '''
        if not os.path.isdir(self.opts.args.output):
            try:
                os.mkdir(self.opts.args.output)
            except Exception:
                self.result = 9
                return
        
        '''
        verify the log file
        if the log file does not exist, create one
        '''
        dirpath = os.path.abspath(self.opts.args.output)
        self.logfilepath = dirpath + "\\" + self.opts.args.log
        try:
            if not os.path.isfile(self.logfilepath):
                fo = open(self.logfilepath,'w')
                fo.close()
        except Exception:
            self.result = 12
            return
        
        '''
        secure mode must be either yes or no
        ignore lower and upper case
        '''
        if not re.match('yes',self.opts.args.mode,flags=re.I) and \
           not re.match('no',self.opts.args.mode,flags=re.I):
            self.result = 11
            return
        
        '''
        user name and password handling
        under secure mode, user name and password are mandatory
        '''
        if re.match('yes',self.opts.args.mode,flags=re.I):
            if not bool(self.opts.args.user):
                self.opts.args.user = input("Please input username: ")
            if not bool(self.opts.args.password):
                self.opts.args.password = getpass.getpass("Please input password: ")
        else:
            self.httphead = 'http://'
            
        '''
        ssl certification verify must be either True or False
        '''
        if not re.match('True',str(self.opts.args.verify)) and \
           not re.match('False',str(self.opts.args.verify)):
            self.result = 13
            return
            
        
       
        
        
        

        
        
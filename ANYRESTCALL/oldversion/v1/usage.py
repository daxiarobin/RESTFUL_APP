'''
Purpose: read and process the input arguments
Author: Yifeng Shen
Versoin: 1.0
Change History:
2019-01-24: v1.0 YS Create the 1st version
'''
import getopt
import sys,os
import re
import getpass
class UsAge(object):
    
    def __init__(self,argv,version,programmname):
        self.argv = argv
        self.version = version
        self.programmname = programmname
        
        '''
        result: 0 - no error 
        '''
        self.result = 0
        
        self.server = ""
        self.port = 12443
        self.outputdic = os.path.abspath(os.path.join(os.path.dirname(__file__), './output'))
        
        '''
        urifile: the actual file which contains a list of the uris
        uri: the single uri
        Either urifile or uri must be specified
        '''
        self.urifile = ""
        self.uri = ""
        
        '''
        urilist: This is a internal variable which contains 
                 all the uris which user specified.
                 No matter user only specify one uri or a uri file,
                 all the uri will be saved in this list.
        '''
        self.urilist = []
        
        '''
        securemode and httphead:   
           yes - https://   (default)
           no  - http://
                     
        '''
        self.securemode = "yes"
        self.httphead = "https://"
        
        '''
        If securemode is yes (https://), then username and password are mandatory
        There are 2 ways to input username/password
           Option 1: via "-d" and "-e" option 
           Option 2: based on the user input prompt
        '''
        self.username = ""
        self.password = ""
        
        '''
        opttype:  get or post
                  default is get
        '''
        self.opttype = "get"
        
        '''
        logfilename: the name of the logfile
        '''
        self.logfilename = self.programmname + ".log"
        self.logfilepath = ""
        
        '''
        sslverification: True or False, default is False
        '''
        self.sslverification = False
        
        
        '''
        construct hash for short and long arg
        key: short arg, eg "s"
        value: long arg, eg "server"
        '''
        self.inputarghash = {}
        self.inputarghash["h"] = "help"
        self.inputarghash["s"] = "server"
        self.inputarghash["p"] = "port"
        self.inputarghash["u"] = "uri"
        self.inputarghash["o"] = "output"
        self.inputarghash["f"] = "file"
        self.inputarghash["t"] = "type"
        self.inputarghash["d"] = "user"
        self.inputarghash["e"] = "password"
        self.inputarghash["m"] = "mode"
        self.inputarghash["l"] = "log"
        self.inputarghash["v"] = "verify"
        
        '''
        construct default short argument list
        '''
        self.shortarglist = []
        self.longarglist = []
        for shortarg in self.inputarghash:
            self.shortarglist.append(shortarg)
            self.longarglist.append(self.inputarghash[shortarg])
            
        self.shortargstring = ""
        matachpattern = r'^h$'
        for tmpstr in self.shortarglist:
            if re.match(matachpattern,tmpstr):
                self.shortargstring = self.shortargstring + tmpstr
            else:
                self.shortargstring = self.shortargstring + tmpstr + ":"
        self.shortargstring = "\"" + self.shortargstring + "\""
        
        '''
        constructd default long argument list
        '''
        self.longargstrlist = []
        matachpattern = r'^'+self.inputarghash["h"]+'$'
        for tmpstr in self.longarglist:
            if not re.match(matachpattern,tmpstr):
                tmpstr = tmpstr+"="
            self.longargstrlist.append(tmpstr)
        '''
        construct hash for arg description
        key: short arg. eg "s"
        valur: description, eg "ip address or server name...."
        '''
        self.argdesc = {}
        self.argdesc["s"] = 'ip address or server name of the target server which provides REST API'
        self.argdesc["p"] = 'REST API server port, default is 12443'
        self.argdesc["u"] = 'single uri for REST API call,'+\
            '\n\t\t\tEg: com.oiforum.json/ndm/network/1/endpoint'
        self.argdesc["f"] = 'file contains the uri list for REST API call,'+\
            '\n\t\t\tEg: Eg: C:\data\mylist.txt'
        self.argdesc["t"] = 'REST call type, get or post, default is get'
        self.argdesc["d"] = 'user name for the REST call'
        self.argdesc["e"] = 'password for the REST call'
        self.argdesc["m"] = 'secure (yes) or non-secure (no) mode for the REST call, default is yes'
        self.argdesc["o"] = 'output directory for all the results, default is ./output'
        self.argdesc["h"] = 'Printing help information'
        self.argdesc["l"] = 'name of the log file, optional'
        self.argdesc["v"] = 'SSL certification verification, True or False. Default is False'
        
        '''
        construnct the mandatory/optional hash for args
        '''
        self.mandatoryhash={}
        for tmpstr in self.argdesc:
            self.mandatoryhash[tmpstr] = "O"
        self.mandatoryhash["s"] = "M"
        self.mandatoryhash["u"] = "M|O"
        self.mandatoryhash["f"] = "M|O"

        
        
    def readInput(self):
        try:
            opts,args = getopt.getopt(self.argv,self.shortargstring,\
                                              self.longargstrlist)  
                                              
        except getopt.GetoptError:
            self.result = 3
        
        for opt,arg in opts:
            if opt in ('-h','--help'):
                self.printUsage()
                self.result = 10
                return self.result,self.securemode,self.httphead,self.server,self.port,\
                           self.urilist,self.opttype,self.username,self.password,\
                           self.outputdic,self.logfilepath,self.sslverification                
            elif opt in ("-s","--server"):
                self.server = arg
            elif opt in ("-p","--port"):
                self.port = arg
            elif opt in ("-u","--uri"):
                self.uri = arg
            elif opt in ("-o","--output"):
                self.outputdic = arg
            elif opt in ("-f","--file"):
                self.urifile = arg
            elif opt in ("-t","--type"):
                self.opttype = arg
            elif opt in ("-d","--user"):
                self.username = arg
            elif opt in ("-e","--password"):
                self.password = arg
            elif opt in ("-m","--mode"):
                self.securemode = arg
            elif opt in ("-l","--log"):
                self.logfile = arg
            elif opt in ("-v","--verify"):
                self.sslverification = arg             
                
        self.validateInput()
        
        return self.result,self.securemode,self.httphead,self.server,self.port,\
                   self.urilist,self.opttype,self.username,self.password,\
                   self.outputdic,self.logfilepath,self.sslverification        
       
        
    def validateInput(self):
        '''
        This function is used to validate all the user input
        '''
        
        '''
        check whether the server address is provided or not
        '''
        if not bool(self.server):
            self.result = 4
            return
        
        '''
        check whether the server port is availabe or not
        '''
        if not bool(self.port):
            self.result = 5
            return        
        
        '''
        uri or uri list file must be specified
        '''
        if not bool(self.uri) and not bool(self.urifile):
            self.result = 6
            return
        
        '''
        construct the internal uri list
        '''
        if bool(self.uri):
            self.urilist.append(self.uri.rstrip())
        
        if bool(self.urifile):
            if not os.path.isfile(self.urifile):
                self.result = 7
                return
            else:
                try:
                    fo = open(self.urifile,'r')
                    for line in fo:
                        self.urilist.append(line.rstrip())
                    fo.close()
                except Exception:
                    self.result = 8
                    return
    
        '''
        verify the output directory
        '''
        if not os.path.isdir(self.outputdic):
            try:
                os.mkdir(self.outputdic)
            except Exception:
                self.result = 9 
                return
        '''
        verify the log file
        if the log file does not exist, create one
        '''
        dirpath = os.path.abspath(self.outputdic)
        self.logfilepath = dirpath + "\\" + self.logfilename
        try:
            if not os.path.isfile(self.logfilepath):
                fo = open(self.logfilepath,'w')
                fo.close()
        except Exception:
            self.result = 12
            return
            
        '''
        verify the input value of secure mode option
        it must be either yes or no
        '''
        if not re.match('yes',self.securemode,flags=re.I) and \
           not re.match('no',self.securemode,flags=re.I):
            self.result = 11
            return
        
        
        '''
        user name and password handling
        under secure mode, user name and password are mandatory
        '''
        if re.match('yes',self.securemode,flags=re.I):
            if not bool(self.username):
                self.username = input("Please input username: ")
            if not bool(self.password):
                self.password = getpass.getpass("Please input password: ")
        else:
            self.httphead = "http://"
            
        '''
        ssl certification must be either True or False
        '''
        if not re.match('True',str(self.sslverification)) and \
           not re.match('False',str(self.sslverification)):
            self.result = 13
            return
                 
    def printUsage(self):
        print ('\nVersoin: '+ self.version)
        print ('\nUsage:')
        print (self.programmname+ ' [-s <server address>] [-p <server port>] \
[-u <uri>] [-o <output directory>][-f <uri list file>]'+'\n\t'+\
        ' [-t <get|post>] [-d <user name>] [-e <password>][-m <yes|no>][-l <logfile>]'\
        + '[-v <True|False>]')
        print ('\nOptions:\n')
        
        for tmpstr in self.argdesc:
            optname = "-"+tmpstr+"|--"+self.inputarghash[tmpstr]+\
                " ("+self.mandatoryhash[tmpstr]+")"
            print ('%20s:' % (optname) + '\t'+ self.argdesc[tmpstr]+'\n')     
        
        
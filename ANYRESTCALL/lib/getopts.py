'''
Functions to handle user input options
Author: Yifeng Shen
Version: 2.0
Change history:
v1.0	2018-08-24	Y.Shen	Created first version
v2.0    2019-01-29      Y.Shen  Re-structured the code
'''
import argparse,os,sys,getpass
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), './'))
if libpath not in sys.path:
    sys.path.append(libpath)
from inputopts import InputOpts

class GetOpts(object):
    '''
    Build default option objecdt list
    '''
    optionlist = []
    optionnamelist = []
    
    _inputopt = InputOpts()
    _inputopt.optname = 's'
    _inputopt.longoptname = 'server'
    _inputopt.longdes = 'ip address or server name of the target server which provides REST API'
    _inputopt.shortdes = 'server address'
    _inputopt.manstr = 'M'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)    
    
    _inputopt = InputOpts()
    _inputopt.optname = 'p'
    _inputopt.longoptname = 'port'
    _inputopt.longdes = 'REST API server port, default is 12443'
    _inputopt.shortdes = 'server port'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname) 
    
    _inputopt = InputOpts()
    _inputopt.optname = 'u'
    _inputopt.longoptname = 'uri'
    _inputopt.longdes = 'single uri for REST API call,'+\
        '\n\t\t\tEg: com.oiforum.json/ndm/network/1/endpoint'
    _inputopt.shortdes = 'uri'
    _inputopt.manstr = 'M|O'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 'f'
    _inputopt.longoptname = 'file'
    _inputopt.longdes = 'file contains the uri list for REST API call,'+\
        '\n\t\t\tEg: Eg: C:\data\mylist.txt'
    _inputopt.shortdes = 'uri list file'
    _inputopt.manstr = 'M|O'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 't'
    _inputopt.longoptname = 'type'
    _inputopt.longdes = 'REST call type, get or post, default is get'
    _inputopt.shortdes = 'get|post'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 'd'
    _inputopt.longoptname = 'user'
    _inputopt.longdes = 'user name for the REST call'
    _inputopt.shortdes = 'get|post'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 'e'
    _inputopt.longoptname = 'password'
    _inputopt.longdes = 'password for the REST call'
    _inputopt.shortdes = 'get|post'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 'm'
    _inputopt.longoptname = 'mode'
    _inputopt.longdes = 'secure (yes) or non-secure (no) mode for the REST call, default is yes'
    _inputopt.shortdes = 'yes|no'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    
    _inputopt = InputOpts()
    _inputopt.optname = 'o'
    _inputopt.longoptname = 'output'
    _inputopt.longdes = 'output directory for all the results, default is ./output'
    _inputopt.shortdes = 'output directory'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)
    
    _inputopt = InputOpts()
    _inputopt.optname = 'l'
    _inputopt.longoptname = 'log'
    _inputopt.longdes = 'name of the log file, optiona'
    _inputopt.shortdes = 'logfile'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname) 
    
    _inputopt = InputOpts()
    _inputopt.optname = 'v'
    _inputopt.longoptname = 'verify'
    _inputopt.longdes = 'SSL certification verification, True or False. Default is False'
    _inputopt.shortdes = 'True|False'
    optionlist.append(_inputopt)
    optionnamelist.append(_inputopt.optname)     
    
    def __init__(self,version,programmname,optlist_add=[],optlist_del=[]):
        self.version = version
        self.programmname = programmname
        
        '''
        Step 1: Construct option description list
        The elements in this list are all InputOpts objects.
        
        Step 2: Read and store the input values
        
        :param
               optlist_add - list of InputOpts objects to be added
               optlist_del - list of option names (string only) to be removed
        '''
        
        '''
        add new options
        '''
        for _opt in optlist_add:
            self.optionlist.append(_opt)
            
        '''
        remove the options which are not required
        '''
        for _optname in optlist_del:
            for _opt in self.optionlist:
                if _opt.optname == _optname:
                    self.optionlist.remove(_opt)
        
        '''
        define the return code, this value is used to determine
        whether there is error when initiating the object
        '''
        self.result = 0
        
        '''
        read the input
        '''
        self.parser = argparse.ArgumentParser()
        
        for _opt in self.optionlist:
            self.parser.add_argument(('-' + _opt.optname),('--' + _opt.longoptname),\
                                     required=_opt.mandatory,help=_opt.longdes)
        
        self.args = self.parser.parse_args()
        
    def printUsage(self):
        print ('\nVersoin: '+ self.version)
        print ('\nUsage:')
        
        '''
        construct the short description list of the input arg
        '''
        shortdesclist = '\n'+self.programmname+'   '
        
        i=0
        for _opt in self.optionlist:
            i=i+1
            j=i%4
            tmpstr = '[-' + _opt.optname + ' <' + _opt.shortdes + '>] '
            if j == 0:
                shortdesclist = shortdesclist + '\n\t   '+ tmpstr
            else:
                shortdesclist = shortdesclist + tmpstr
        print (shortdesclist)
        print ('\nOptions:\n')
        
        '''
        print long description args
        '''
        for _opt in self.optionlist:
            tmpstr = '-' + _opt.optname + '|--' + _opt.longoptname +\
                ' (' + _opt.manstr + ')'
            print ('%20s:' %(tmpstr) + '\t' + _opt.longdes + '\n')
            
        
    
    
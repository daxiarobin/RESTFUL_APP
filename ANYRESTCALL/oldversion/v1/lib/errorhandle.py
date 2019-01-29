'''
Throw the error message based on the error code
'''

import sys
import os

libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/'))
if libpath not in sys.path:
    sys.path.append(libpath)
from errorcode import ErrorCode

class Error(object):
    def __init__(self):
        '''
        ''' 
        self.err = ErrorCode()

    def thrownmsg(self,code):
        msg=self.returnmsg(code)
        print ("\n"+msg)
        return msg

    def returnmsg(self,code):
        return {
            self.err.NOERROR: 'All completed!',
            self.err.MISSINGOPT:'Error: Missing mandatory options',
            self.err.NOOUTPUTDIC: 'Error: Unable to access output directory',
            self.err.SYNTAXERROR: 'Error: Syntax error, wrong options specified',
            self.err.PRTHELP: '',
            self.err.MISSINGSERVER: 'Error: Missing the server address',
            self.err.MISSINGPORT: 'Error: Missing the server port',
            self.err.MISSINGURI: 'Error: uri or uri list file must be specified',
            self.err.NOURILISTFILE: 'Error: uri list file specified does not exist',
            self.err.ACCESSFAILURIFILE: 'Error: unable to access the uri list file',
            self.err.MKDIRFAIL: 'Error: unable to create output directory',
            self.err.WRONGSECUREMODE: 'Error: securemode must be either yes or no',
            self.err.LOGFILEFAIL: 'Error: unable to create log file',
            self.err.WRONGSSLVERIFY:'Error: SSL verification must be True or False',
            self.err.UNKNOWNERROR: 'Error: Unkown error'            
            }.get(code,"Error: Unknown error")
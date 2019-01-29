'''
Purpose: Class to end the programm
Author: Yifeng Shen
Create data: 2019-01-24
Version: 1.0
Change history:
2019-01-24 v1.0 YS create the first version
'''

from errorhandle import Error
import sys

class EndProgramm(object):
    error = Error()
    def __init__(self):
        '''
        '''
        
    def terminate(self,result,fo):
        self.error.thrownmsg(result)
        try:
            if not fo.closed:
                fo.close()
        except Exception:
            '''
            '''
        sys.exit(0)
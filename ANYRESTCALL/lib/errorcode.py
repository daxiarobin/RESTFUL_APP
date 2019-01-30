'''
Purpose: mapping between error code name and value
'''

class ErrorCode(object):
    '''
    No error: 0
    '''
    NOERROR = 0
    
    '''
    Missing mandatory input: 1
    Eg: user forget to input a argument which is mandatory (M)
    '''
    MISSINGOPT = 1
    
    '''
    Unable to access output directory
    Eg: no access right or no privilledge to create
    '''
    NOOUTPUTDIC = 2
    
    '''
    Syntax error which is due to "getopt.GetoptError"
    '''
    SYNTAXERROR = 3
    
    '''
    Missing the server ip address
    '''
    MISSINGSERVER = 4
    
    '''
    Missing the server port
    '''
    MISSINGPORT = 5
    
    '''
    Missing uri or uri list file
    '''
    MISSINGURI = 6
    
    '''
    uri list file does not exist
    '''
    NOURILISTFILE = 7
    
    '''
    uri list file is not readable
    '''
    ACCESSFAILURIFILE = 8
    
    '''
    not able to create output directory
    '''
    MKDIRFAIL = 9
    
    '''
    Print help information
    '''
    PRTHELP = 10
    
    '''
    input value for secure mode option is not yes or no
    '''
    WRONGSECUREMODE = 11
    
    '''
    unable to create log file
    '''
    LOGFILEFAIL = 12
    
    '''
    Wrong SSL verification option
    It must be either True or False
    '''
    WRONGSSLVERIFY = 13
    
    '''
    REST GET fail
    '''
    RESTGETFAIL = 14
    
    '''
    REST PUT fail
    '''
    RESTPUTFAIL = 15
    
    '''
    REST POST fail
    '''
    RESTPOSTFAIL = 16
    
    '''
    REST UPDATE fail
    '''
    RESTUPDATEFAIL = 17
    
    '''
    unable to connect to RESTFUL server
    '''
    CONNFAIL = 18
    '''
    Unknown error: 100
    Not sure what is the error, reserved as unknown
    '''
    UNKNOWNERROR = 100
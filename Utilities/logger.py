import logging
from Config.variables import Variables
class Logger():
    
    #-----LOGGER INIT-----#

    # returns logStringIO logger
    def initStringIOLogger(logStringioObj, loggerName):
        # return a logger with the specified name, creating it if necessary
        logger = logging.getLogger(loggerName)
        # set level, initialze the log handler and set logger's format
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        ioLogHandler = logging.StreamHandler(logStringioObj)
        ioLogHandler.setFormatter(formatter)
        # add the specified handler to the logger
        logger.addHandler(ioLogHandler)
        return logger

    # returns txt file logger
    def initLoggertxt(fileName):
        path = 'C:\\Test Automation\\Logs\\'
        # return a logger with the specified name, creating it if necessary
        logger = logging.getLogger('name_%s' % fileName) 
        # set level, initialze the log handler ina  file and set logger's format
        logger.setLevel(logging.INFO) 
        handler = logging.FileHandler(path + fileName + ".log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s') #5
        handler.setFormatter(formatter)
        # add the specified handler to the logger
        logger.addHandler(handler)
        return logger
    
    # initialize txt or string IO logger depending on the execution agent
    def initLogger(name, logStringIO):
        if Variables.executionAgent == "chromeLocal":
            logger = Logger.initLoggertxt(name)
        elif Variables.executionAgent == "chromeRemote":
            logger = Logger.initStringIOLogger(logStringIO, name)
        return logger
    
    #-----FILECHECKERS-----#

    # returns the number of a keyword appearances in a stringIO log
    def fileCheckerStringIO(stringIO, keyword):
        found = 0
        # gets the log
        datafile = stringIO.getvalue() 
        # parse to string and split lines
        for line in str(datafile).splitlines():
            if keyword in line:
                found += 1     
        return found

    # returns the number of a keyword appearances in a txt log
    def fileCheckertxt(fileName, keyword):
        path = ''
        found = 0
        # get the log
        with open(path + fileName +".log") as f:
            datafile = f.readlines()
        for line in datafile:
            if keyword in line:
                found += 1
        return found
    
    # returns a dict with key-value pairs with data from the txt log,
    # the key corresponds with the keyword and the value corresponds to the number of appearances
    def fileCheckerFailedtxt(file):
        dict_failed = {}
        dict_failed['failed_steps'] = Logger.fileCheckertxt(file, 'FAIL-')
        dict_failed['failed_steps_assertions'] = Logger.fileCheckertxt(file, 'FAIL-ASSERTIONS')
        dict_failed['failed_steps_populate'] = Logger.fileCheckertxt(file, 'FAIL-POPULATEFIELDS:')
        dict_failed['locator_error'] = Logger.fileCheckertxt(file, 'FAIL-LOCATORERROR')
        dict_failed['masterdata_error'] = Logger.fileCheckertxt(file, 'FAIL-MASTERDATA:')
        dict_failed['unexecuted'] = Logger.fileCheckertxt(file, 'FAIL-UNEXECUTED:')
        dict_failed['fail_step_archetypes'] = Logger.fileCheckertxt(file, 'FAIL-STEP:')
        dict_failed['fail_check'] = Logger.fileCheckertxt(file, 'FAIL-CHECK:')
        dict_failed['fail_access'] = Logger.fileCheckertxt(file, 'FAIL-ACCESS:')
        return dict_failed

    # returns a dict with key-value pairs with data from the string IO log,
    # the key corresponds with the keyword and the value corresponds to the number of appearances
    def fileCheckerFailedStringIO(stringIo):
        dict_failed = {}
        dict_failed['failed_steps'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-')
        dict_failed['failed_steps_assertions'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-ASSERTIONS')
        dict_failed['failed_steps_populate'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-POPULATEFIELDS:')
        dict_failed['locator_error'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-LOCATORERROR')
        dict_failed['masterdata_error'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-MASTERDATA:')
        dict_failed['unexecuted'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-UNEXECUTED:')
        dict_failed['fail_step_archetypes'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-STEP:')
        dict_failed['fail_check'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-CHECK:')
        dict_failed['fail_access'] = Logger.fileCheckerStringIO(stringIo, 'FAIL-ACCESS:')
        return dict_failed
    
    # returns a dict with key-value pairs with data from the txt log,
    # the key corresponds with the keyword and the value corresponds to the number of appearances
    def fileCheckerPassedtxt(file):
        dict_passed = {}
        dict_passed['passed_steps'] = Logger.fileCheckertxt(file, 'PASS')
        dict_passed['passed_steps_assertions'] = Logger.fileCheckertxt(file, 'PASS-ASSERTIONS')
        dict_passed['pass_step_archetypes'] = Logger.fileCheckertxt(file, 'PASS-STEP:')
        dict_passed['pass_check'] = Logger.fileCheckertxt(file, 'PASS-CHECK:')
        return dict_passed

    # returns a dict with key-value pairs with data from the string IO log,
    # the key corresponds with the keyword and the value corresponds to the number of appearances
    def fileCheckerPassedStringIO(stringIo):
        dict_passed = {}
        dict_passed['passed_steps'] = Logger.fileCheckerStringIO(stringIo, 'PASS')
        dict_passed['passed_steps_assertions'] = Logger.fileCheckerStringIO(stringIo, 'PASS-ASSERTIONS')
        dict_passed['pass_step_archetypes'] = Logger.fileCheckerStringIO(stringIo, 'PASS-STEP:')
        dict_passed['pass_check'] = Logger.fileCheckerStringIO(stringIo, 'PASS-CHECK:')
        return dict_passed
    
    # checks fail keywords in txt or string IO log depending on the execution agent
    def fileCheckerFailed(file, stringIO):
        if Variables.executionAgent == 'chromeLocal':
            dict_failed = Logger.fileCheckerFailedtxt(file)
        elif Variables.executionAgent == 'chromeRemote':
            dict_failed = Logger.fileCheckerFailedStringIO(stringIO)
        return dict_failed

    # checks pass keywords in txt or string IO log depending on the execution agent
    def fileCheckerPassed(file, stringIO):
        if Variables.executionAgent == 'chromeLocal':
            dict_passed = Logger.fileCheckerPassedtxt(file)
        elif Variables.executionAgent == 'chromeRemote':
            dict_passed = Logger.fileCheckerPassedStringIO(stringIO)
        return dict_passed



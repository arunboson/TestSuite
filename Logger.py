import logging
import time
import os

def getPythonTestFiles(path=None):    
    files = [] 
    files_in_directory = os.listdir(path)
    for File in files_in_directory:
        if File.endswith('.py'):
            if "__init__" not in File :
                files.append(File)
    return files

def getfilename():
    start_time = time.ctime()
    [day,month,date,timestamp,year] = start_time.split(' ')
    [a,b,c] = timestamp.split(':')
    timestamp = a + '_' + b + '_' + c
    log_file_name = "test_" + timestamp + ".log" 
    return log_file_name

def getLogger(logFilePath='C:\\Results\\'):
    file_name = logFilePath + getfilename() 
    logging.basicConfig(filename= file_name, filemode='w', format='%(asctime)s - %(message)s',datefmt='%H:%M:%S', level=logging.INFO)
    logger = logging.getLogger('testlogger')    
    return logger

def getReportFile():
    loc_time = time.localtime()
    filename = 'C:\Results\Reports\Report_' + str(loc_time.tm_mday) + '_' + str(loc_time.tm_mon) + '_' + str(loc_time.tm_year) + '_' + str(loc_time.tm_hour) + '_' + str(loc_time.tm_min) + '_' + str(loc_time.tm_sec) + '.csv'
    csv_file = open(filename,'w')
    csv_file.write('TestID,Result\n')
    return csv_file

def passlog(testlogger):
    testlogger.info("######     ##       #####    #####")
    testlogger.info("##   ##   ####     ##       ##")
    testlogger.info("##   ##  ##  ##    ##       ##")
    testlogger.info("######  ########    #####    #####")
    testlogger.info("##     ##      ##       ##       ##")
    testlogger.info("##    ##        ##      ##       ##")
    testlogger.info("##   ##          ## #####   ######")
    
def faillog(testlogger):
    testlogger.info("######      ##       ###### ##")
    testlogger.info("##         ####        ##   ##")
    testlogger.info("##        ##  ##       ##   ##")
    testlogger.info("######   ########      ##   ##")
    testlogger.info("##      ##      ##     ##   ##")
    testlogger.info("##     ##        ##    ##   ##")
    testlogger.info("##    ##          ## ###### #######")    
import sys
import time
import os
import random
import time
import CanBus
import UART
import CommandLineArguments
import Logger

testlogger = None

def getPythonTestFiles(path=None):    
    files = [] 
    files_in_directory = os.listdir(path)
    for File in files_in_directory:
        if File.endswith('.py') and File.startswith('Test'):
            files.append(File)
    return files

def main():    
    #initializing objects for use
    global testlogger
    testlogger = Logger.getLogger()                                                         #get logger
    testlogger.info("Test Starts at %s",time.ctime())                                       #initial log
    CmdLineArgObject  = CommandLineArguments.CommandLineArgs(sys.argv,testlogger)           #get CommandLineArgs
    CmdLineArgObject.printValues()                                                          #printValues
    randObj = random.Random(CmdLineArgObject.randomSeed)
    
    #Create Excel File for Report
    file = Logger.getReportFile()
    
    #initialize CAN object
    CanObj = CanBus.CanBus(logger=testlogger)
    
    #initialize UART Object
    UartBus = UART.SerialBus(baudrate=115200,COM=CmdLineArgObject.COMport,logger=testlogger)
    
    #find the test files we need 
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '\Tests'
    testlogger.info("Looking for a files in path = %s "% dir_path)
    testFiles = getPythonTestFiles(dir_path)
    sys.path.append(dir_path)
    
    #if only test has to be run then add only that test in 
    if CmdLineArgObject.TestID != None :
        testFound = False
        for testname in testFiles:
            if testname.startswith(CmdLineArgObject.TestID):
                testFound = True
                testFiles.clear()
                testFiles.append(testname)
                break
        if testFound == False :
            testlogger.info("Wrong testID = %s",CmdLineArgObject.TestID)
            raise 
        
    #start importing tests one by one
    for testname in testFiles :
        testname = testname[:-3]
        moduleObj = __import__(testname)
        testObj = moduleObj.TestProcedure(testlogger,randObj,CanObj,UartBus)
        cycles = CmdLineArgObject.CycleCount 
        while cycles:
            testlogger.info("--"*20)
            testlogger.info("Running test = %s",testname)
            testlogger.info("--"*20)
            testObj.Run()
            cycles -= 1
        testlogger.info("--"*20)
        if testObj.EndOfOperation() == True :
            testlogger.info("%s is passed...!"%testname)				
            file.write(testname+','+'Pass\n')
            Logger.passlog(testlogger)
        else:
            testlogger.info("%s is failed...!"%testname)
            file.write(testname+','+'Fail\n')
            Logger.faillog(testlogger)
    file.close()

if __name__ == "__main__":
    main()
import os
import sys

class CommandLineArgs( object ):
    def __init__(self,argv,logger):
        self.CycleCount = 0
        self.TestID     = None
        self.COMport    = 'COM9'
        self.testDuration = 1800   # in seconds default value = half hour
        self.randomSeed = None
        self.logFilePath = "C:\Results"
        self.logger = logger
        argument_list = argv
        self.CmdLineArgumentDict = {}
        for i in range(1, len(argument_list)):
            key,data = argument_list[i].split('=')
            hyphon,param = key.split('--')
            if param.lower() == 'Cyclecount'.lower() :
                self.CycleCount = int(data)
            elif param.lower() == 'testID'.lower() :
                self.TestID = data
            elif param.lower() == 'testDuration'.lower():
                if 'h' in data.lower() :
                    self.testDuration = int(data.split('h')[0]) * 3600
                elif 'm' in data.lower() :
                    self.testDuration = int(data.split('h')[0]) * 60
                elif 's' in data.lower() :
                    self.testDuration = int(data.split('h')[0])
                else :
                    self.logger.info("Wrong value inputted")
                    raise
            elif param.lower() == 'randomSeed'.lower() :
                self.randomSeed = int(data)
            elif param.lower() == 'logFilePath'.lower() :
                self.logFilePath = data
            elif param.lower() == 'COMport'.lower():
                self.COMport = data.upper()
        
        #if randomSeed is not passed take it randomly        
        if self.randomSeed == None:
            import random
            self.randomSeed = random.Random().seed
    
    def printValues(self):
        self.logger.info("--"*12)
        self.logger.info("Test Parameters are set as: ")
        self.logger.info("Cyclecount   = %d",self.CycleCount)
        self.logger.info("randomSeed   = %d",self.randomSeed)
        self.logger.info("testDuration = %d seconds",self.testDuration)
        self.logger.info("testID       = %d",self.TestID)
        self.logger.info("COM port     = %s",self.COMport)
        self.logger.info("logFilePath  = %s",self.logFilePath)
        self.logger.info("--"*12)
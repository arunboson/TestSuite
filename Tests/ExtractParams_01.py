############################################################################
## TestID = ExtractParam01
## Author : Akshay Godase
## Date   : 18/04/2019
## Description : This test reads all the inputs to imx and logs them if
## wrong input is recieved test fails
## this test compares parameters received number of parameters from paramfile
############################################################################

import sys
import os
import logging
import numpy
import time
sys.path.append('..')
import SevconLib

class TestProcedure( object ):
    def __init__( self,logger,randomObj, canObj, uartObj):
        self.logger = logger
        self.randomObj = randomObj
        self.logger.info("Inside __init__ constructor of file %s",__file__)
        self.canBus = canObj
        self.serialBus = uartObj
        self.didItPass = True
        return
    # end of method

    def Run( self ):
        self.didItPass = True
        self.logger.info("Inside Run Method didItPass set to True initially")
        uart_failure = 0
        expected_param = 33
        check_samples = 200
        expected = self.get_number_of_param()
        self.logger.info("Waiting for ECU to initiate...!")
        time.sleep(4) #init time for ECU
        
        while(check_samples):
            #read UART string from ECU    
            rcvd_string = self.serialBus.read()
            if rcvd_string != None and len(rcvd_string) <= 800:
                self.logger.info("string received = %s",rcvd_string)
                param_dict = SevconLib.extract_param_from_string(string=rcvd_string)
                no_of_parameters = len(param_dict.keys())
                if  no_of_parameters ==  expected:
                    self.logger.info("Parameters received as expected = %d",no_of_parameters)
                else :
                    self.logger.info("Failed since Parameters received = %d",no_of_parameters)
                    self.didItPass = False
            else :
                if rcvd_string != None and len(rcvd_string) > 800 :
                    self.logger.info("Message is too large.......!")
                    raise 
                uart_failure += 1
                self.logger.info("string didn't receive %d times....!",uart_failure)
                if uart_failure == 5 :
                    self.logger.info("Uart has failed so leaving the test with failure...")    
                    self.didItPass = False
            check_samples -= 1
        return
    # end of method
    
    #this function gives us number of parameters
    def get_number_of_param( self ):
        paramfilepath = os.getcwd()
        paramFile = open(paramfilepath + '\Tests\param.txt')
        param_count = 0
        for count in paramFile:
            param_count += 1
        self.logger.info("Number of parameters in configure file = %d",param_count)
        return param_count
        #end
    
    def EndOfOperation( self ):
        self.logger.info("Inside end operation")
        return self.didItPass
    # end of method
# end of class


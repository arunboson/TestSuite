############################################################################
## TestID = RPM01_all_values_of_RPM
## Author : Akshay Godase
## Date   : 18/04/2019
## Description : This test inputs all values of RPM range specified by
## SEVCON and check if ECU recieves same or not
############################################################################

import sys
import os
import logging
import numpy
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
        sevconID = 0x361
        uart_failure = 0
        lower_RPM_limit = -200
        higher_RPM_limit = 200
        wrong_string = 0
        
        for RPM in range(lower_RPM_limit,higher_RPM_limit+1) :
            data = SevconLib.getRPMbytes(RPM)
            expected = RPM
            #send CAN message to ECU
            status = self.canBus.send(msg_id=sevconID,data=data,is_extended_id=False,timeout=0)
            if status == True :
                self.logger.info("CAN message sent successfuly!")
            else :
                self.logger.info("CAN message sending Failed..!")
            
            #read UART string from ECU    
            rcvd_string = self.serialBus.read()
            if rcvd_string != None and len(rcvd_string) >= 10:
                self.logger.info("string received = %s",rcvd_string)
                param_dict = SevconLib.extract_param_from_string(string=rcvd_string)
                if param_dict == None :
                    wrong_string += 1
                    self.logger.info("Lets ignore this string and increased wrong string count = %d",wrong_string)
                    if wrong_string >= 5 :
                        self.didItPass = False
                        self.logger.info("5 wrong string recieved hence failing test case")
                        return
                if expected == param_dict['RPM'] :
                    self.logger.info("Pass")
                else :
                    self.logger.info("Fail")
                    self.didItPass = False
            else :
                uart_failure += 1
                self.logger.info("string didn't receive %d times....!",uart_failure)
                if uart_failure == 5 :
                    self.logger.info("Uart has failed so leaving the test with failure...")    
                    self.didItPass = False
                    return
        self.logger.info("Tested all the possible values from %d to %d",lower_RPM_limit,higher_RPM_limit)

        return
    # end of method
    
    def EndOfOperation( self ):
        self.logger.info("Inside end operation")
        return self.didItPass
    # end of method
# end of class
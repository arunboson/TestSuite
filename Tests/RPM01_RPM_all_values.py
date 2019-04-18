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
from .. import SevconLib

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
        sevconID = 0x298
        
        for RPM in range(-20000,20001) :
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
            self.logger.info("string received = %s",rcvd_string)
            param_dict = SevconLib.extract_param_from_string(string=rcvd_string)
            if expected == param_dict['RPM'] :
                self.logger.info("Pass")
            else :
                self.logger.info("Fail")
                self.didItPass = False
            self.logger.info("Tested all the possible values from -20000 to 20000")

        return
    # end of method
    
    def EndOfOperation( self ):
        self.logger.info("Inside end operation")
        return self.didItPass
    # end of method
# end of class
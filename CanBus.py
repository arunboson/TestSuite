import can

class CanBus( object ) :
    def __init__(self, logger, bustype='ixxat', channel=0, bitrate=250000) :
        self.logger = logger
        self.logger.info("Initializing CAN bus with param: bustype= %s channel= %d bitrate= %d",bustype,channel,bitrate)
        try :
            self.bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
        except :
            self.logger.info("CAN initialization failed..! Please check ixxat connection...!")
            return None
    
    def send(self,msg_id,data,is_extended_id,timeout=0):
        msg = can.Message(arbitration_id= msg_id, data= data, extended_id= is_extended_id)
        try :
            self.bus.send(msg,timeout)
            return True
        except :
            self.logger.info("Message not sent!")
            return False
    def rcv(self,timeout=0):
        return self.bus.recv(timeout)
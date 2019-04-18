import serial

class SerialBus( object ):
    def __init__ (self,logger,baudrate=115200,COM='COM9'):
        self.serialObject = serial.Serial()
        self.serialObject.baudrate = baudrate;
        self.serialObject.port = COM
        self.serialObject.timeout = 2       #initializing with serial read timeout = 2 seconds
        self.logger = logger
        did_it_open = self.serialObject.open()    
    
        if did_it_open is False :
            self.logger.info("Serial Port Configuration Failed")
            raise
        else :
            self.logger.info("Serial Port Configured with baudrate = %d COM Port = %s",baudrate,COM)            
            
    def send(self,buffer):
        try:
            self.serialObject.write(buffer)
            return True
        except:
            self.logger.info("Sending Failed.....!")
            return False
    
    def read(self,buffersize=-1):
        try :
            x = self.serialObject.readline()
            x= x.decode()
            x = x.rsplit('\r\n')[0]
            x = x.rsplit('\n')[0]
            return x            
        except :
            return None
        
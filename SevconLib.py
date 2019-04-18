import numpy

#this function will give us the values data bytes for particular motor temp value
def getMotorTempbytes(MotorTemp):
    newMotorTemp = numpy.int16(MotorTemp)
    data = bytearray(8)
    data[5] = data[4] = data[3] = data[2] = data[1] = data[0] = 0
    data[6] = numpy.uint8(newMotorTemp)
    data[7] = numpy.uint8(newMotorTemp>>8)
    return data

#this function will give us the values data bytes for particular sevcon temp value
def sevconTempbytes(sevTemp):
    newSevTemp = numpy.int16(sevTemp)
    data = bytearray(8)
    data[7] = data[5] = data[4] = data[6] = data[2] = data[1] = data[0] = 0
    data[3] = numpy.uint8(newSevTemp)
    return data 

#this function will give us the values data bytes for particular sevcon capVolts value
def capVoltageBytes(capVolts):
    newCapVolts = numpy.int16(capVolts)
    data = bytearray(8)
    data[5] = data[4] = data[3] = data[2] = data[7] = data[6] = 0
    data[0] = numpy.uint8(newCapVolts)
    data[1] = numpy.uint8(newCapVolts>>8)
    return data 

#this function will give us the values data bytes for particular battery current value
def batt_i_Bytes(batt_i):
    batt_i_16bit = numpy.int16(batt_i)
    data = bytearray(8)
    data[7] = data[6] = data[3] = data[2] = data[1] = data[0] = 0
    data[4] = numpy.uint8(batt_i_16bit)
    data[5] = numpy.uint8(batt_i_16bit>>8)
    return data 

#this function will give us the values data bytes for particular RPM value
def getRPMbytes(RPM):
    newRPM = numpy.int16(RPM)
    data = bytearray(8)
    data[3] = data[2] = data[1] = data[0] = 0
    data[4] = numpy.uint8(newRPM)
    data[5] = numpy.uint8(newRPM>>8)
    data[6] = numpy.uint8(newRPM>>16)
    data[7] = numpy.uint8(newRPM>>24)
    return data

#this function will take the string from ECU and extract param into dictionary
def extract_param_from_string(string):
    param_dict = {}
    list_of_param = string.split(' ')
    for i in range(len(list_of_param)):
        try :
            param,value = list_of_param[i].split(':')
            value = int(value)
            param_dict[param] = (value)
        except :
            #wrong value
            pass    
    return param_dict
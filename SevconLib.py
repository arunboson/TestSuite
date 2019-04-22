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
    newCapVolts = numpy.uint16(capVolts)
    data = bytearray(8)
    data[5] = data[4] = data[3] = data[2] = data[7] = data[6] = 0
    data[0] = numpy.uint8(newCapVolts)
    data[1] = numpy.uint8(newCapVolts>>8)
    return data 

#this function will give us the values data bytes for particular battery current value
def batt_i_Bytes(batt_i):
    batt_i_16bit = numpy.int16(batt_i)
    data = bytearray(8)
    data[7] = data[6] = data[5] = data[2] = data[1] = data[0] = 0
    data[3] = numpy.uint8(batt_i_16bit)
    data[4] = numpy.uint8(batt_i_16bit>>8)
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
    list_of_param = string.split('|')
    for i in range(len(list_of_param)):
        try :
            param,value = list_of_param[i].split(':')
        except :
            #wrong string recieved  ignore
            return None
        if '.' in value :
            #float type value
            value = float(value)
        elif 'true' in value :
            #value is bool type true
            value = True
        elif 'false' in value :
            #value in bool type false
            value = False
        elif param == 'ID' :
            value = value.split(' ')[1]
        elif param == 'FaultLevel':
            value = value.split(' ')[1]
        else :
            try :
                value = int(value)
            except :
                value = value.split(' ')[1]
        param_dict[param] = (value)
    return param_dict
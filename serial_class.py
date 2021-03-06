import serial
import numpy as np

from image_prep import *

class Serial:
    def __init__(self, COM):
        self.com = COM

    def serial_begin(self, *COM):
        if len(COM)==1:
            self.com = COM[0]
        self.serialPort = serial.Serial(port = self.com, baudrate=115200,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    def serial_send(self, image_array):
        image = image_array.astype(np.uint8)
        data = bytearray(image)
        self.serialPort.write(bytes(data))

    def serial_receive_int(self):
        if(self.serialPort.in_waiting >= 1):
            serialString = self.serialPort.read(1)
            return int.from_bytes(serialString, "big")
        else:
            return -1 # No data in buffer

    def serial_receive_float(self):
        if(self.serialPort.in_waiting >= 4):
            serialString = self.serialPort.read(4)
            data_bytes = np.array(serialString)
            data_as_float = data_bytes.view(dtype=np.float32)
            return data_as_float
        else:
            return -1 # No data in buffer
    
    def serial_receive_32bit_uint(self):
        if(self.serialPort.in_waiting >= 4):
            serialString = self.serialPort.read(4)
            data_bytes = np.array(serialString)
            data_as_float = data_bytes.view(dtype=np.uint32)
            return data_as_float
        else:
            return -1 # No data in buffer
        
    '''Start: Add 16bit integer number support'''
    def serial_receive_16bit_uint(self):
        if(self.serialPort.in_waiting >= 2):
            serialString = self.serialPort.read(2)
            data_bytes = np.array(serialString)
            data_as_int16 = data_bytes.view(dtype=np.uint16)
            return data_as_int16
        else:
            return -1 # No data in buffer
    '''End'''

    def get_serial_status(self):
        return self.serialPort.is_open

    def serial_close(self):
        serialPort.close()

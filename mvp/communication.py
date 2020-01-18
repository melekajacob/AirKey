import serial
import numpy as np
import time


class ArduinoInterface(object):
    """docstring for ResistanceValues"""

    def __init__(self):
        # self.ser = serial.Serial('/dev/cu.usbmodem14201', 9600) #Ryan's Port
        time.sleep(.5)
        self.serR = serial.Serial('/COM8', 9600)  # Sufiyaan's Port
        self.serL = serial.Serial('/COM9', 9600)  # Sufiyaan's Port

    def get_resistance_values(self):
        self.serL.write(b"send")
        self.serR.write(b"send")

        line = self.serL.readline()

        resistanceValues = np.zeros(10)

        for i in range(0, 10):
            # print(i)
            if i < 5:
                line = self.serL.readline()
            else:
                line = self.serR.readline()
            resistanceValues[i] = float(line.replace(b"\r\n", b""))

        return resistanceValues

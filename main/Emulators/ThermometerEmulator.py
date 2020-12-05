'''
Author: Ifiok Udoh

'''
import ThermalSensor

#Class for thermal Camera Emulator
class ThermometerEmulator(ThermalSensor.ThermalSensor):
    def __init__(self):
        super(ThermometerEmulator, self).__init__(17,25)
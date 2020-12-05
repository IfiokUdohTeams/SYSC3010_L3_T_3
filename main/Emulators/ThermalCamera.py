'''
Author: Ifiok Udoh

'''
import ThermalSensor

#Class for thermal Camera Emulator 
class ThermalCamera(ThermalSensor.ThermalSensor):
    def __init__(self):
        super(ThermalCamera, self).__init__(30,45)


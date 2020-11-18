# Vaccine Class File                                                                                                          #
# date: Nov 15 2020                                                                                                           #
# name: Harshil Verma                                                                                                         #
# description: This class file contians methods for getting and setting temperature values. IMPORTS: RVLClass & SenseHatClass #

import SenseHatClass

class Vaccine():
    def __init__(self):
        self.temperature = ""
        self.pressure = ""
   
    
    def setTemperature(self, temp):
        self.temperature = temp
        
    def getTemperature(self):
        return self.temperature
    
    def getPressure(self):
        return self.pressure
    
    def setPressure(self, press):
        self.pressure = press   
        



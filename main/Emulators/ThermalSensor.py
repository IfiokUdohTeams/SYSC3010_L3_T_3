#Thermometer emulator that generates random temperature continously
#Author Ifiok Udoh
#
import random
import time
import threading
class ThermalSensor(object):

    """
    random_Temp Continously generates Random temperature value within limits start 
    and stop
    """
    def random_Temp(self, start, stop):
        while(self._generate == 1):
            self.mutex.acquire() #make sure object mutex is acquired to prevent temperature from being read while new temperaure is being generated
            self._temperature = random.randint(start,stop)
            self.mutex.release()

    """
    __init__ initializes a ThermalSensor Object
    """
    def __init__(self,min,max):
        self.mutex = threading.Lock() #initialize mutex for Synchronization
        self._temperature = 0 
        self._generate = 1
        self._tempThread = threading.Thread(target=self.random_Temp, args=(min, max)) # generate random temperature in a different Thread
        self._tempThread.start()
        

    """
    read returns the current temperature res of a ThermalSensor Object
    """
    def read(self):
        time.sleep(1) #read delay
        self.mutex.acquire()
        res =  self._temperature
        self.mutex.release()
        return res

    """
    Close stops thread that generates random temperature for ThermalSensor Object
    """
    def close(self):
        self._generate = 0


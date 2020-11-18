#Thermometer emulator that generates random temperature continously
#Author Ifiok Udoh
#
import random
import time
import threading
class ThermalSensor(object):

    """
    Continously generates Random temperature value within limits start 
    and stop
    """
    def random_Temp(self, start, stop):
        while(self._generate == 1):
            # print(stop)
            self.mutex.acquire()
            self._temperature = random.randint(start,stop)
            self.mutex.release()

    def __init__(self,min,max):
        self.mutex = threading.Lock()
        self._temperature = 0 
        self._generate = 1
        self._tempThread = threading.Thread(target=self.random_Temp, args=(min, max)) # random human temperature
        self._tempThread.start()
        

    def read(self):
        time.sleep(1) #read delay
        self.mutex.acquire()
        res =  self._temperature
        self.mutex.release()
        return res

    def close(self):
        self._generate = 0

# def main():
#     thermo = thermometer()
#     print("here")
#     print(thermo.read())
#     thermo.close()

# if __name__ == "__main__":
#     main()
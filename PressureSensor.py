#Thermometer emulator that generates random temperature continously
#Author Ifiok Udoh
#
import random
import time
import threading
class PressureSensor(object):

    """
    Continously generates Random temperature value within limits start 
    and stop
    """
    def random_pressure(self, start, stop):
        while(self._generate == 1):
            # print(stop)
            self.mutex.acquire()
            self._pressure = random.randint(start,stop)
            self.mutex.release()

    def __init__(self,min,max):
        self.mutex = threading.Lock()
        self._pressure = 0 
        self._generate = 1
        self._pressureThread = threading.Thread(target=self.random_pressure, args=(min, max)) # random pressure
        self._pressureThread.start()
        

    def read(self):
        time.sleep(1) #read delay
        self.mutex.acquire()
        res =  self._pressure
        self.mutex.release()
        return res

    def close(self):
        self._generate = 0

# def main():
#     pressSensor = PressureSensor(0,5)
#     print("here")
#     print(pressSensor.read())
#     pressSensor.close()

# if __name__ == "__main__":
#     main()
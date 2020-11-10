import unittest
import read
import write
import time

class TestLabData(unittest.TestCase):
    def test_temp(self):
        for x in range(10):
                time.sleep(15)  #wait for 15 seconds here because Thingspeak refreshes every 15s.
                write.temperature()
        read.read_temp()
        self.assertEqual(write.tempA, read.t)
        
    def test_pres(self):
        for x in range(10):
                time.sleep(15)
                write.pressure()
        read.read_pres()
        self.assertEqual(write.presA, read.u)    


if __name__ == '__main__':
            unittest.main()

from random import randint
import unittest
import time
import sys
sys.path.append('..')
from Headquaters import Headquaters


class TestLabData(unittest.TestCase):  

        def test_temp_pressure(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"
                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                

                headquaters.closeAll()#close connection to read or write to TS channel
                
                self.assertEqual([0,1,2,3,4,5,6,7,8,9], headquaters.ReadList)    


if __name__ == '__main__':
            unittest.main()
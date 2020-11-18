from random import randint
import unittest
import time
import sys
sys.path.append('..')
from Headquaters import Headquaters
from RVL import RemoteVaccineLab


class TestLabData(unittest.TestCase):  

        def test_temp_pressure(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"
                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                remotevaccinelab = RemoteVaccineLab.RemoteVaccineLab(TSC,readKey, writeKey)

                #generate list of 10 random data to send
                remotevaccinelab.generateRandomTempPress(headquaters.node_id)
                time.sleep(1)# To ensure all reads are completed

                headquaters.closeAll()#close connection to read or write to TS channel
                remotevaccinelab.closeAll()

                # self.assertEqual(1, 1)  
                self.assertEqual(int(headquaters.vaccineLabTemp), 20)
                self.assertEqual(int(headquaters.vaccineLabPress), 10)
                  


if __name__ == '__main__':
            unittest.main()
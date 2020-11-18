import sys
sys.path.append('..')
from Headquaters import Headquaters
from RVL import RemoteVaccineLab
from random import randint
import unittest
import time


class TestLabData(unittest.TestCase):  

        def test_temp_pressure(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"
                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                remoteVaccinelab = RemoteVaccineLab.RemoteVaccineLab(TSC,readKey, writeKey)
                headquaters.app_client()
                remoteVaccinelab.app_client()

                while(remoteVaccinelab.done != True):
                    pass

                headquaters.close()#close connection to read or write to TS channel
                headquaters.app_clientClose()#close connection to android app
                remoteVaccinelab.close()
                remoteVaccinelab.app_clientClose()

                self.assertEqual(int(remoteVaccinelab.PressureThreshold), 10)
                self.assertEqual(int(remoteVaccinelab.TempThreshold), 20)
                self.assertEqual(int(headquaters.pressThreshold), int(remoteVaccinelab.PressureThreshold))
                self.assertEqual(int(headquaters.tempThreshold), int(remoteVaccinelab.tempThreshold))
                    


if __name__ == '__main__':
            unittest.main()
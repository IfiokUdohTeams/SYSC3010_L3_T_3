from random import randint
import unittest
import time
import sys
sys.path.append('..')
from Headquaters import Headquaters
from RPL import RemotePatientLab, Patient
from Emulators import ThermalCamera


class TestLabData(unittest.TestCase):  

        def test_temp_pressure(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"

                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                remotepatientLab = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)
                remotepatientLab.tempThreshold = 30
                
                # thermalCamera = ThermalCamera.ThermalCamera()      
                # temp1 = thermalCamera.read()
                
                patient1 = Patient.Patient("John","32","Male")
                patient1.setTemperature(40)
                remotepatientLab.newPatient(patient1)


                time.sleep(1)# To ensure all reads are completed

                headquaters.closeAll()#close connection to read or write to TS channel
                remotepatientLab.closeAll()

                # self.assertEqual(1, 1)  
                self.assertEqual(int(headquaters.patientTemp), 40)
                
                  


if __name__ == '__main__':
            unittest.main()
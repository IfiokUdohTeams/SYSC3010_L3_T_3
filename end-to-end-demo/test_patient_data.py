from random import randint
import unittest
import time
import Headquaters
import RemotePatientLab
import RemoteVaccineLab


class TestData(unittest.TestCase):
    
    def test_PatientTemperature(self):
    # Initialize nodes in communication path
        TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
        readKey = '0'
        writeKey = "OEGCYO9F8FJCZGO6"
        headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
        remotepatientlab = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)

        #generate list of 10  data in range 1 to 10 to send
        temp_thresh = range(1,10)
        for data in temp_thresh:
            headquaters.Format_and_Write(remotepatientlab.node_id, data) #send data from Headquaters to Remote patient
            
        time.sleep(1)# To ensure all reads are completed

        headquaters.close()#close connection to read or write to TS channel
        remotepatientlab.close()

        self.assertIn(1,remotepatientlab.ReadList)
        self.assertIn(9,remotepatientlab.ReadList)
        self.assertIn(5,remotepatientlab.ReadList)
        self.assertNotIn(50,remotepatientlab.ReadList)
        self.assertNotIn(15,remotepatientlab.ReadList)
        
        
if __name__=='__main__':
    unittest.main()
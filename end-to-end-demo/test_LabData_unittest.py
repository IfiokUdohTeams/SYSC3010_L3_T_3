from random import randint
import unittest
import time
import Headquaters
import RemotePatientLab
import RemoteVaccineLab


class TestLabData(unittest.TestCase):  

        def test_temp_pressure(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"
                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                remotepatientlab = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)

                #generate list of 10 random data to send
                temperature_pressure = []
                for x in range(10):
                        #Generate 10 random readings
                        random = randint(10, 100)
                        temperature_pressure.append(random)

                for data in temperature_pressure:
                        remotepatientlab.Format_and_Write(headquaters.node_id, data) #send data from Remote patient lab to Headquaters
                time.sleep(1)# To ensure all reads are completed

                headquaters.close()#close connection to read or write to TS channel
                remotepatientlab.close()

                self.assertEqual(temperature_pressure, headquaters.ReadList)    


if __name__ == '__main__':
            unittest.main()

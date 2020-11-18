from random import randint
import unittest
import time
import sys
sys.path.append('..')
from Headquaters import Headquaters


class TestHeadquater(unittest.TestCase):  

        def test_Headquater(self):
                # Initialize nodes in communication path
                TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
                readKey = '0'
                writeKey = "OEGCYO9F8FJCZGO6"

                headquaters = Headquaters.Headquaters(TSC,readKey, writeKey)
                headquaters.createDatabase()
                noOfEntries = randint(1,11)
                for i in range(noOfEntries):
                    headquaters.addToDataBase(randint(18,20))

                entries = headquaters.getDBEntriesCnt()


                time.sleep(1)# To ensure all reads are completed
                headquaters.clearDB()
                headquaters.closeAll()#close connection to read or write to TS channel

                # self.assertEqual(1, 1)  
                self.assertEqual(entries, noOfEntries)

if __name__ == '__main__':
            unittest.main()
from random import randint
import unittest
import time
import sys
sys.path.append('..')
from RPL import RemotePatientLab

# Initialize nodes in communication path
TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
readKey = '0'
writeKey = "OEGCYO9F8FJCZGO6"
remotepatientlab = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)

#generate list of 10 random data to send
temperature_pressure = []
for x in range(10):
        #Generate 10 random readings
        temperature_pressure.append(x)

for data in temperature_pressure:
        remotepatientlab.Format_and_Write("headquaters","end" + "," + str(data)) #send data from Remote patient lab to Headquaters

remotepatientlab.close()
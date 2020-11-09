import httplib
import urllib
import time
from random import randint

tempA = [ ]
presA = [ ]
key = "1GW1O9Z7PCYY8AXV"  # Put your API Key here

def temperature():
    for x in range(10):
        
        #Generate 10 random temperature readings
        temp = randint(10, 100)
        tempA.append(temp)
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            data = response.read()
            conn.close()
        except:
            print "connection failed"


    
def pressure():
    for x in range(10):
        
        #Generate 10 random pressure readings
        pres = randint(500, 2000)
        presA.append(pres)
        params = urllib.urlencode({'field2': pres, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print pres
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        

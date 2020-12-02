import sys
import os
import ConfigProcessor
import httplib
import urllib
import requests
import time

def cleanup():
    #cleanup Test directory
    if os.path.exists("Test/RPL.db"):
        os.remove("Test/RPL.db")

    if os.path.exists("Test/RVL.db"):
        os.remove("Test/RVL.db")

    if os.path.exists("Test/Threshold.db"):
        os.remove("Test/Threshold.db")

    if os.path.exists("Test/headquatersEntries"):
        os.remove("Test/headquatersEntries")

    if os.path.exists("Test/remoteVaccineLab1Entries"):
        os.remove("Test/remoteVaccineLab1Entries")

    if os.path.exists("Test/remoteVaccineLab2Entries"):
        os.remove("Test/remoteVaccineLab2Entries")

    if os.path.exists("Test/remotePatientLabEntries"):
        os.remove("Test/remotePatientLabEntries")

    #cleanup current directory
    if os.path.exists("RPL.db"):
        os.remove("RPL.db")

    if os.path.exists("RVL.db"):
        os.remove("RVL.db")

    if os.path.exists("Threshold.db"):
        os.remove("Threshold.db")

    if os.path.exists("headquatersEntries"):
        os.remove("headquatersEntries")

    if os.path.exists("remoteVaccineLab1Entries"):
        os.remove("remoteVaccineLab1Entries")

    if os.path.exists("remoteVaccineLab2Entries"):
        os.remove("remoteVaccineLab2Entries")

    if os.path.exists("remotePatientLabEntries"):
        os.remove("remotePatientLabEntries")

config = ConfigProcessor.ConfigProcessor()

def write(sender, receiver):
    field1 = '{"sender" : ' + '"' + sender + '"' +  ", " + '"receiver" : ' + '"' + receiver + '"' + '}'
    responeData = ''
    params = urllib.urlencode({'field1': field1, 'field2': "cleanup", 'key':config.writeKey}) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        responeData = response.read()
        conn.close()
    except:
        print("connection failed")
        
    return responeData

def clearThingSpeak():
    responeData = ''
    parameters = urllib.urlencode({'api_key':'KKZVCHC88LSZSAN2'})
    try:
        responeData = requests.delete("https://api.thingspeak.com/channels/1161330/feeds.json",params=parameters)
    except:
        print("connection failed")
    


def main():
    cleanup()
    nodes = ["headquaters", "remoteVaccineLab1", "remoteVaccineLab2", "remotePatientLab"]
    for i in nodes:
        if i != config.node:
            write(config.node,i)
    time.sleep(30)
    clearThingSpeak()
    

if __name__ == "__main__":
    main()


    
import urllib
import requests
import httplib
import threading
import json
import random
import write
import time
import unittest
# Define a function that will read the server 
t=[]
u=[]
 
def read_temp():
    URL='https://api.thingspeak.com/channels/1224062/feeds.json?api_key=WHM1IEG6FTN1XOEG&results=10'
    KEY='WHM1IEG6FTN1XOEG'
    HEADER='&results=10'
    NEW_URL=URL+KEY+HEADER
    print(URL)

    get_data=requests.get(URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']

    field1=get_data['feeds']
    print(field1)
    
    for x in field1:
        print(x['field1'])
        t.append(x['field1'])
        
    print t
    


def read_pres():
    URL='https://api.thingspeak.com/channels/1224062/feeds.json?api_key=WHM1IEG6FTN1XOEG&results=10'
    KEY='WHM1IEG6FTN1XOEG'
    HEADER='&results=10'
    NEW_URL=URL+KEY+HEADER
    print(URL)

    get_data=requests.get(URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']

    field2=get_data['feeds']
    print(field2)
    
    for y in field2:
        print(y['field2'])
        u.append(y['field2'])
        
    print u

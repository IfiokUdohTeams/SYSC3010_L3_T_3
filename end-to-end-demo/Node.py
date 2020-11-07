'''
DO NOT EDIT
Author: Ifiok Udoh
'''

from ctypes import *
import ChannelReader
import threading
import httplib
import urllib
import time
import requests
import json

class Node(object):
    def __init__(self, thingSpeak_url, readKey, writeKey, node_id):
        self.writeKey = writeKey
        self.readKey = readKey
        self.processThread = ''
        self.mutex = threading.Lock()
        self.threads = []
       
        self.node_id = node_id
        self.read_data_pointer = pointer(c_wchar_p(""))
        self.read_sender_pointer = pointer(c_wchar_p(""))
        self.write_data = ''
        self.channelReader = ChannelReader.ChannelReader(thingSpeak_url, self.readKey, self.node_id, 
                                                        self.read_data_pointer, self.read_sender_pointer, self.mutex)

        self.channelReader.poll()
        self.Process()

        self.threads.append(self.channelReader.poll_thread)
        self.threads.append(self.processThread)
        self.write_data = []

    #processes data based on specification from communication protocol table for node type
    def process_data(self):
        print("READ: ", self.read_data_pointer[0])

    #Synchronixes readThinkchannel with processing data
    def synchronize(self):
        while(True):
            self.mutex.acquire()
            if self.read_data_pointer[0] != "":
                self.process_data()
                self.read_data_pointer[0] = ""
            self.mutex.release()

    def Process(self):
        self.processThread = threading.Thread(target=self.synchronize,)
        self.processThread.start()

    def field1(self,receiver):
        sender = self.node_id
        field1 = '{"sender" : ' + '"' + sender + '"' +  ", " + '"receiver" : ' + '"' + receiver + '"' + '}'
        return field1
    
    #used to format in specific node format
    def FormatData(self,receiver,data):
        self.field1(receiver)
        self.write_data = [self.field1(self.node_id),data]

    def write(self):
        responeData = ''
        params = urllib.urlencode({'field1': self.write_data[0], 'field2': self.write_data[1], 'key':self.writeKey}) 
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

    #used to write formatted data to TS
    def Format_and_Write(self,receiver,data):
        self.FormatData(receiver, data) #make sure data is formatted before a write operation
        while(self.write() == '0'):
            time.sleep(5)
        
        


# hq = Node('https://api.thingspeak.com/channels/1161330/feeds.json?',0, "OEGCYO9F8FJCZGO6", 'headquaters')

# hq.Format_and_Write("headquaters", "testing1")

# hq.Format_and_Write("headquaters", "testing2")


        

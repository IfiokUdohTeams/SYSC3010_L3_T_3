'''
DO NOT EDIT
Author: Ifiok Udoh
'''
from ctypes import *
import time
import requests
import json
import random
import threading

'''
Channel reader instantiates a channel reader object that polls specified TS channel for data
'''
class ChannelReader:
    def __init__(self,channel_url,key,node_id, data_pointer, sender_pointer, mutex):
        self.entries = 0
        self.key=key
        self.channel_url = channel_url
        self.node_id = node_id
        self.data_pointer = data_pointer
        self.sender_pointer = sender_pointer
        self.poll_thread = ""
        self.mutex = mutex
        self.run = True


    def read_data_thingspeak(self):
        while(self.run):
            get_data=requests.get(self.channel_url).json()
            current_last_entry_id = get_data['channel']['last_entry_id']

            #update entrycount to stay up to date on enry/entries written to channel
            if current_last_entry_id > self.entries:
                feeds =get_data['feeds'][self.entries:(current_last_entry_id)]
                self.entries = current_last_entry_id

                #for sender and receiver identifier
                for x in feeds:
                    if json.loads(x['field1'])['receiver'] == self.node_id:
                        self.mutex.acquire()
                        self.data_pointer[0] = x['field2']
                        self.sender_pointer[0] = json.loads(x['field1'])['sender']
                        self.mutex.release()
             
            if current_last_entry_id == None:
                self.entries= 0
        
        
    def poll(self):
        self.poll_thread = threading.Thread(target=self.read_data_thingspeak,)
        self.poll_thread.start()

    def close(self):
        self.run = False

       


        


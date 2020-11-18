import sys
sys.path.append('..')
from Communication import Node
import socket
import threading
import random

class RemoteVaccineLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(RemoteVaccineLab, self).__init__(thingSpeak_url, readKey, writeKey,"remoteVaccineLab")
        self.host = '192.168.0.52'
        self.port = 8080
        self.socket = socket.socket()  # instantiate
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(0)
        print("connected!")
        self.recvThread = ""
        self.cond = True
        self.changeTempBy = "0"
        self.changePressBy = "0"
        self.PressureThreshold = "0"
        self.TempThreshold = "0"
        self.done = False #temp

    # def FormatData(self,data):


    def process_data(self):
        print("remoteVaccineLab READ: ", self.read_data_pointer[0], " from: " ,self.read_sender_pointer[0])
        if(self.read_sender_pointer[0] == "headquaters"):
            read = self.read_data_pointer[0]
            read = read.split(",")
            self.PressureThreshold = read[0]
            self.TempThreshold = read[1]
            self.done = True #temp



    def RcvAppData(self):
        rawdata = ""
        while(self.cond):
            try:
                rawdata = self.socket.recv(1024).decode()  # receive response
            except socket.error:
                pass
            if rawdata != "":
                data = rawdata.split("\n")
                # data = rawdata
                print(data)
                opcode = data[0]
                if opcode == "R":
                    print("here")
                    self.socket.send("changeTempBy:" + self.changeTempBy + "," + "changePressBy:" +
                    self.changePressBy +"," + "PressureThreshold:" + self.PressureThreshold +"," + "TempThreshold:" + self.TempThreshold + "\n")
                    print("sent")


    def app_client(self):
        self.recvThread = threading.Thread(target=self.RcvAppData,)
        self.recvThread.start()

    def app_clientClose(self):
        self.cond = False
        self.socket.close()

    def generateRandomTempPress(self, receiver):
        for x in range(9):
            #Generate 10 random readings
            temp = random.randint(10, 100)
            pressure = random.randint(10, 100)
            
            self.Format_and_Write(receiver, "temp:" + str(temp) + "," + "pressure:" + str(pressure))
        self.Format_and_Write(receiver, "temp:" + str(20) + "," + "pressure:" + str(10))

    def closeAll(self):
        self.close()
        self.app_clientClose()

# if __name__ == "__main__":
#     TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
#     readKey = '0'
#     writeKey = "OEGCYO9F8FJCZGO6"
#     test = RemoteVaccineLab(TSC,readKey, writeKey)
#     test.app_client()

import sys
sys.path.append('..')
from Communication import Node
import socket
import threading 

class Headquaters(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(Headquaters, self).__init__(thingSpeak_url, readKey, writeKey,"headquaters")
        self.host = '192.168.0.52'
        self.port = 8080
        self.socket = socket.socket()  # instantiate
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(0)
        print("connected!")
        self.recvThread = ""
        self.cond = True
        self.pressThreshold = ""
        self.tempThreshold = ""
        self.vaccineLabTemp = ""
        self.vaccineLabPress = ""
        self.done = False
        self.ReadList = []


    def process_data(self):
        # print("headquaters READ: ", self.read_data_pointer[0].encode("ascii"), " from: ", self.read_sender_pointer[0])
        # a =  self.read_data_pointer[0]
        # self.ReadList.append(int(a.encode("ascii"))) # encode read unicode string to ascii and convert to integer
        if(self.pressThreshold != "" and self.tempThreshold != ""):
            self.writeToThresholdDatabase()
            self.Format_and_Write("remoteVaccineLab", self.pressThreshold + "," + self.tempThreshold)
            self.pressThreshold = ""
            self.tempThreshold = ""
        elif(self.read_sender_pointer[0] == "remoteVaccineLab"):
            rawdata = self.read_data_pointer[0]
            data = rawdata.split(",")
            print(data)
            print("here")
            self.vaccineLabTemp = data[0].split(":")[1]
            self.vaccineLabPress = data[1].split(":")[1]
            self.done = True
        elif(self.read_sender_pointer[0] == "remotePatientLab"):
            a =  self.read_data_pointer[0]
            self.ReadList.append(int(a.encode("ascii")))



    def RcvAppData(self):
        rawdata = ""
        while(self.cond):
            try:
                rawdata = self.socket.recv(1024).decode()  # receive response
            except socket.error:
                pass
            
            # print("here1")
            if rawdata != "":
                data = rawdata.split(",")
                print(data)
                opcode = data[0]
                if opcode == "S":
                    print("here")
                    self.pressThreshold = data[1].split(":")[1]
                    self.tempThreshold = data[2].split(":")[1]
                    self.process_data()


    def app_client(self):
        self.recvThread = threading.Thread(target=self.RcvAppData,)
        self.recvThread.start()

    def app_clientClose(self):
        self.socket.close()
        self.cond = False
        print("closed")
        

    def writeToThresholdDatabase(self):
        pass

    def closeAll(self):
        self.close()
        self.app_clientClose()
    

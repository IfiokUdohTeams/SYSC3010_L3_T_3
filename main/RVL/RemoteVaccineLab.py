'''
Authors: Zoya Mushtaq, Ifiok Udoh

'''
import sys
sys.path.append('..')
from Communication import Node
import socket
import threading
import random
import sense_emu
import sense_hat
import time
import cleanup

class RemoteVaccineLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey, RVL, host, pollTime, sense):
        super(RemoteVaccineLab, self).__init__(thingSpeak_url, readKey, writeKey, RVL)
        self.pollThread = ""
        self.host               = host
        self.port               = 8080
        self.socket             = socket.socket()  # instantiate
        if sense == "emu":
            self.sense              = sense_emu.SenseHat() #senseHat Emulator
        else:
            self.sense              = sense_hat.SenseHat() #senseHat Hardware
        self.recvThread         = ""
        self.cond               = True
        self.changeTempBy       = "0"
        self.changePressBy      = "0"
        self.PressureThreshold  = 0
        self.TempThreshold      = 0
        self.currentTemperature = 0
        self.currentPressure    = 0
        self.pollTempandPressure(pollTime)
        self.done               = False #temp

    def ConnectToAndroidApp(self):
        try:
            self.socket.connect((self.host, self.port))
        except:
            pass
        else:
            print("connected to Android APP!")
            self.socket.setblocking(0)
            self.app_client()


    def process_data(self):
        if self.read_data_pointer[0] == "cleanup":
            cleanup.cleanup()
            self.closeAll()
            
        else:
            print("remoteVaccineLab READ: ", self.read_data_pointer[0], " from: " ,self.read_sender_pointer[0])
            if(self.read_sender_pointer[0] == "headquaters"):
                read = self.read_data_pointer[0]
                read = read.split(",")
                self.PressureThreshold = int(read[0])
                self.TempThreshold = int(read[1])
                self.done = True #temp

    def read_Temperature(self):
        self.currentTemperature = round(self.sense.get_temperature()) #fxn get_temperature will give value measured by sense hat in degress celcuis whihc will be stored in temp variable 
        message = ' T=%dC ' %(self.currentTemperature) #store temp, with a specific notation in "message" string 
        self.sense.show_message(message, scroll_speed=(0.08), text_colour=[200,240,200], back_colour=[0, 0, 0]) #call in which i can send any message to my sense hat display screen. passing message string
        # time.sleep(4)

    def read_Pressure(self): 
        self.currentPressure = round(self.sense.get_pressure())   
        message = 'P=%d ' %(self.currentPressure) #store pressure,  with a specific notation in "message" string 
        self.sense.show_message(message, scroll_speed=(0.08), text_colour=[200,240,200], back_colour=[0, 0, 0]) #call in which i can send any message to my sense hat display screen. passing message string
        # time.sleep(4)

    def pollTempandPressure(self, refreshTime):
        self.pollThread = threading.Timer(refreshTime, self.pollTempandPressure, (refreshTime,) )
        self.pollThread.start()
        self.read_Temperature()
        self.read_Pressure()
        self.Format_and_Write("headquaters", "time:" + str(time.time()) + "," + "temp:" + str(self.currentTemperature) + "," + "pressure:" + str(self.currentPressure) + "," + "tempThreshold:" + str(self.TempThreshold) + "," + "pressureThreshold:" + str(self.PressureThreshold))


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
                    diffTemp = self.currentTemperature - self.TempThreshold
                    diffPress = self.currentPressure - self.PressureThreshold
                    if diffTemp > 0:
                        self.changeTempBy = "-" + str(diffTemp)
                    else:
                        self.changeTempBy = "+" + str(diffTemp)
                    if diffPress > 0:
                        self.changePressBy = "-" + str(diffPress)
                    else:
                        self.changePressBy = "+" + str(diffPress) 
                
                    self.socket.send("changeTempBy:" + str(self.changeTempBy) + "," + "changePressBy:" +
                    str(self.changePressBy) +"," + "PressureThreshold:" + str(self.PressureThreshold) +"," + "TempThreshold:" + str(self.TempThreshold) + "\n")
                    print("sent")
                rawdata = ""


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
        self.pollThread.cancel()
        self.app_clientClose()


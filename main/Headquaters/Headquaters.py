'''
Authors: Harshil Verma, Linpu Liu, Ifiok Udoh

'''
import sys
sys.path.append('..')
from Communication import Node
import socket
import threading 
import sqlite3
import cleanup

#Headquaters class a subclass of Node
class Headquaters(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey, host):
        self.createDBs()
        super(Headquaters, self).__init__(thingSpeak_url, readKey, writeKey,"headquaters")
        self.socket = socket.socket()  # instantiate socket for connecting to Android APP
        self.port = 8080 #Port number for android app socket
        self.host = host #Ipaddress for android device
        self.recvThread = ""
        self.cond = True
        self.pressThreshold = ""
        self.tempThreshold = ""
        self.vaccineLabTemp = ""
        self.vaccineLabPress = ""
        self.patientTemp = ""
        self.done = False
        self.ReadList = []
        self.ReadCnt = 0
        self.dbconnect = ""

    #initialixes and connects Socket to Android APP
    def ConnectToAndroidApp(self):
        try:
            self.socket.connect((self.host, self.port))
        except:
            pass
        else:
            print("connected to Android APP!")
            self.socket.setblocking(0)
            self.app_client()

    #Overwites Node Process_data Processes gotten data
    def process_data(self):
        if self.read_data_pointer[0] == "cleanup":
            print("got cleanup message")
            cleanup.cleanup()
            self.closeAll()

        if(self.pressThreshold != "" and self.tempThreshold != ""):
            print("headquaters READ: " +  self.pressThreshold + " " + self.tempThreshold + " from: Android APP")
            print("")
            self.Format_and_Write("remoteVaccineLab1", self.pressThreshold + "," + self.tempThreshold)
            self.Format_and_Write("remoteVaccineLab2", self.pressThreshold + "," + self.tempThreshold)
            self.addToThresholdDB(float(self.pressThreshold), float(self.tempThreshold))
            self.pressThreshold = ""
            self.tempThreshold = ""

        elif(self.read_sender_pointer[0] == "remoteVaccineLab1" and self.read_data_pointer[0] != "cleanup"): #process data from vaccineLab
            print("headquaters READ: ", self.read_data_pointer[0].encode("ascii"), " from: ", self.read_sender_pointer[0])
            print("")
            rawdata = self.read_data_pointer[0]
            data = rawdata.split(",")            
            time                                    = float(data[0].split(":")[1])
            self.vaccineLabTemp                     = float(data[1].split(":")[1])
            self.vaccineLabPress                    = float(data[2].split(":")[1])
            Current_Temperature_threshold           = float(data[3].split(":")[1])
            Current_Pressure_threshold              = float(data[4].split(":")[1])
            self.vaccineLabTemp = data[0].split(":")[1]
            self.vaccineLabPress = data[1].split(":")[1]
            self.done = True
            self.addToRVL1DB(time, self.vaccineLabTemp, self.vaccineLabPress, Current_Temperature_threshold, Current_Pressure_threshold)

        elif(self.read_sender_pointer[0] == "remoteVaccineLab2" and self.read_data_pointer[0] != "cleanup"): #process data from vaccineLab
            print("headquaters READ: ", self.read_data_pointer[0].encode("ascii"), " from: ", self.read_sender_pointer[0])
            print("")
            rawdata = self.read_data_pointer[0]
            data = rawdata.split(",")
            time                                    = float(data[0].split(":")[1])
            self.vaccineLabTemp                     = float(data[1].split(":")[1])
            self.vaccineLabPress                    = float(data[2].split(":")[1])
            Current_Temperature_threshold           = float(data[3].split(":")[1])
            Current_Pressure_threshold              = float(data[4].split(":")[1])
            self.vaccineLabTemp = data[0].split(":")[1]
            self.vaccineLabPress = data[1].split(":")[1]
            self.done = True
            self.addToRVL2DB(time, self.vaccineLabTemp, self.vaccineLabPress, Current_Temperature_threshold, Current_Pressure_threshold)
        
        elif(self.read_sender_pointer[0] == "remotePatientLab" and self.read_data_pointer[0] != "cleanup"): #process data from patientLab
            print("headquaters READ: ", self.read_data_pointer[0].encode("ascii"), " from: ", self.read_sender_pointer[0])
            print("")
            rawdata = self.read_data_pointer[0]
            data = rawdata.split(",")
            if data[0] == "end":                                #end-to-end demo
                self.ReadList.append(int(data[1]))
                self.ReadCnt += 1
                if self.ReadCnt == 9:
                    self.done = True
            else:
                time                                    = float(data[0].split(":")[1])
                name                                    = data[1].split(":")[1]
                age                                     = int(data[2].split(":")[1])
                gender                                  = data[3].split(":")[1]
                self.patientTemp                        = float(data[4].split(":")[1])
                Current_Temperature_threshold           = float(data[5].split(":")[1])
                self.Format_and_Write("remotePatientLab", "recievedNewPatient")
                self.addToRPLDB(time, name, age, gender, self.patientTemp, Current_Temperature_threshold)

            
    #REcieves messages from connected Anroid app socket
    def RcvAppData(self):
        rawdata = ""
        while(self.cond):
            try:
                rawdata = self.socket.recv(1024).decode()  # receive response
            except socket.error:
                pass
            
            if rawdata != "":
                data = rawdata.split(",")
                rawdata = ""
                print(data)
                opcode = data[0]
                if opcode == "S":

                    self.pressThreshold = data[1].split(":")[1]
                    self.tempThreshold = data[2].split(":")[1]
                    self.process_data()


    def app_client(self):
        self.recvThread = threading.Thread(target=self.RcvAppData,)
        self.recvThread.start()

    #Closes connection to connected android app socket
    def app_clientClose(self):
        self.socket.close()
        self.cond = False
        print("closed")

    def createRVLDatabase(self):
        self.dbconnect = sqlite3.connect("RVL.db");
        #row_factory to sqlite3.ROw class
        self.dbconnect.row_factory = sqlite3.Row;
        #now we create a cursor to work with db
        cursor = self.dbconnect.cursor();
        #execute insert statement
        cursor.execute('''create table if not exists remoteLab1(time REAL, temperature REAL, pressure REAL, Current_Temperature_threshold REAL, Current_Pressure_threshold REAL)''');
        cursor.execute('''create table if not exists remoteLab2(time REAL, temperature REAL, pressure REAL, Current_Temperature_threshold REAL, Current_Pressure_threshold REAL)''');

        #close the connection
        self.dbconnect.close();

    def addToRVL1DB(self, time, temperature, pressure, Current_Temperature_threshold, Current_Pressure_threshold):
        self.dbconnect = sqlite3.connect("RVL.db");

        cursor = self.dbconnect.cursor();
        cursor.execute('''insert into remoteLab1 values (?, ?, ?, ?, ?)''',(time, temperature, pressure, Current_Temperature_threshold, Current_Pressure_threshold));
        self.dbconnect.commit();
        self.dbconnect.close();

    
    def addToRVL2DB(self, time, temperature, pressure, Current_Temperature_threshold, Current_Pressure_threshold):
        self.dbconnect = sqlite3.connect("RVL.db");

        cursor = self.dbconnect.cursor();
        cursor.execute('''insert into remoteLab2 values (?, ?, ?, ?, ?)''',(time, temperature, pressure, Current_Temperature_threshold, Current_Pressure_threshold));
        self.dbconnect.commit();
        self.dbconnect.close();
    
    
    def clearRVLDB(self):
        self.dbconnect = sqlite3.connect("RVL.db");

        cursor = self.dbconnect.cursor();
        # #clear Databases
        cursor.execute('DELETE FROM remoteLab1');
        cursor.execute('DELETE FROM remoteLab2');
        self.dbconnect.commit()
        self.dbconnect.close();

    def createThresholdDatabase(self):
        self.dbconnect = sqlite3.connect("Threshold.db");
        #row_factory to sqlite3.ROw class
        self.dbconnect.row_factory = sqlite3.Row;
        #now we create a cursor to work with db
        cursor = self.dbconnect.cursor();
        #execute insert statement
        cursor.execute('''create table if not exists threshold(tempThreshold REAL, pressureThreshold REAL)''');

        #close the connection
        self.dbconnect.close();

    def addToThresholdDB(self,pressThreshold, tempThreshold):
        self.dbconnect = sqlite3.connect("Threshold.db");

        cursor = self.dbconnect.cursor();
        cursor.execute('''insert into threshold values (?, ?)''',(tempThreshold, pressThreshold));
        self.dbconnect.commit();
        self.dbconnect.close();

    def clearThresholdDB(self):
        self.dbconnect = sqlite3.connect("Threshold.db");

        cursor = self.dbconnect.cursor();
        # #clear Databases
        cursor.execute('DELETE FROM threshold');
        self.dbconnect.commit()
        self.dbconnect.close();

    def createRPLDatabase(self):
        self.dbconnect = sqlite3.connect("RPL.db");
        #row_factory to sqlite3.ROw class
        self.dbconnect.row_factory = sqlite3.Row;
        #now we create a cursor to work with db
        cursor = self.dbconnect.cursor();
        #execute insert statement
        cursor.execute('''create table if not exists patients(time REAL, name text, age Integer, gender text, temperature REAL, Current_Temperature_threshold REAL)''');

        #close the connection
        self.dbconnect.close();

    def addToRPLDB(self,time, name, age, gender, temperature, Current_Temperature_threshold):
        self.dbconnect = sqlite3.connect("RPL.db");

        cursor = self.dbconnect.cursor();
        cursor.execute('''insert into patients values (?, ?, ?, ?, ?, ?)''',(time, name, age, gender, temperature, Current_Temperature_threshold));
        self.dbconnect.commit();
        self.dbconnect.close();

    def clearRPLDB(self):
        self.dbconnect = sqlite3.connect("RPL.db");

        cursor = self.dbconnect.cursor();
        # #clear Databases
        cursor.execute('DELETE FROM patients');
        self.dbconnect.commit()
        self.dbconnect.close();

    def createDBs(self):
        self.createRPLDatabase()
        self.createRVLDatabase()
        self.createThresholdDatabase()


    def closeAll(self):
        self.close()
        self.app_clientClose()
    

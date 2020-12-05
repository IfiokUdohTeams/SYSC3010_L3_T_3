'''
Authors: Zoya Mushtaq, Ifiok Udoh

'''
import sys
import os
import time
import threading
import select
import tty
import termios
sys.path.append('..')
from Communication import Node
import Patient
import sense_emu
import sense_hat
import cleanup

#Class remote patientlab subclass of Node
class RemotePatientLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey, sense):
        super(RemotePatientLab, self).__init__(thingSpeak_url, readKey, writeKey,"remotePatientLab")
        self.tempThreshold = 30.0
        self.currentPatient = Patient.Patient(None,None,None)
        if sense == "emu":
            self.sense              = sense_emu.SenseHat() #senseHat Emulator
        else:
            self.sense              = sense_hat.SenseHat() #senseHat Hardware
        self.sense.low_light = True
        self.done = False
        self.toClose = False
        self.old_settings = termios.tcgetattr(sys.stdin)
        self.patientPollThread = threading.Thread(target=self.pollNewPatient,)
        self.patientPollThread.start()

    #Polls patient information from terminal   
    def pollNewPatient(self):
        while self.toClose != True:
            print("")
            pname = raw_input("New Patient name: ")
            if pname == "done":
                self.toClose = True
                break
            age = raw_input("New Patient age: ")
            if age == "done":
                self.toClose = True
                break
            gender = raw_input("New Patient gender: ")
            if gender == "done":
                self.toClose = True
                break
            print("Processing Patient...Please Wait")
            print("")
            pat = Patient.Patient(pname,age,gender)
            pat.setTemperature(40)
            self.newPatient(pat)
            while self.done == False:
                pass
            self.done = False

    def process_data(self):
        # print("remotePatientLab READ: " + self.read_data_pointer[0] + " from: " + self.read_sender_pointer[0])
        if self.read_data_pointer[0] == "cleanup":
            cleanup.cleanup()
            self.closeAll()
            
        elif(self.read_data_pointer[0] == "recievedNewPatient"):
            # print("hereRPLrcv")
            self.checkCurrentPatientTemperature()


    def checkCurrentPatientTemperature(self):
        if self.currentPatient.getTemperature() > self.tempThreshold:
            print("Current patient Temperature Above threshold.... \nPlease Push middle button on SenseHat to Continue")
            self.sense.set_pixels(Alarm())
            cond = True
            while cond:
                events = self.sense.stick.get_events()
                if events:
                    for event in events:
                        if event.action == 'pressed' and event.direction == 'middle':
                            print("pressed middle button on SenseHat!")
                            self.sense.clear()
                            cond = False
                            self.done = True
            
        
    def newPatient(self,patient):
        self.currentPatient = patient
        self.Format_and_Write("headquaters","time:" + str(time.time()) + "," + "name:" + patient.getName() + "," +  "age:" + patient.getAge() + "," 
        + "gender:" + patient.getGender() + "," + "temperature:" + str(patient.getTemperature()) + "," + "Current_Temperature_threshold:" + str(self.tempThreshold))

    def closeAll(self):
        self.toClose = True
        self.close()

def Alarm():
    red = (255, 0, 0)
    nothing = (0,0,0)

    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo










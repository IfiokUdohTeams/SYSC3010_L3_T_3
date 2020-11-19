# COVID-19 Lab Simulation
# Remote Patient Lab
# date: Nov 12 2020
# name: Zoya Mushtaq
# description: Remote Patient Lab set up
import sys
sys.path.append('..')
from Communication import Node
import Patient
import sense_emu
import sense_hat

class RemotePatientLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(RemotePatientLab, self).__init__(thingSpeak_url, readKey, writeKey,"remotePatientLab")
        self.tempThreshold = ""
        self.currentPatient = Patient.Patient(None,None,None)
        self.sense = sense_emu.SenseHat()
        self.sense.low_light = True
        self.done = False
        self.pollNewPatient()
        self.close = 0
        # sense = sense_hat.SenseHat() 

    def pollNewPatient(self):
        while self.close != 3:
            name = input("New Patient name: ")
            age = input("New Patient age: ")
            gender = input("New Patient gender: ")
            print("Processing Patient...")
            pat = Patient.Patient(name,age,gender)
            self.newPatient(pat)
            while self.done == False:
                pass
            self.close += 1
            self.done = False

    def process_data(self):
        # print("remotePatientLab READ: ", self.read_data_pointer[0], " from: ", self.read_sender_pointer[0])
        a =  self.read_data_pointer[0]
        print(a)
        # self.ReadList.append(int(a.encode("ascii"))) # encode read unicode string to ascii and convert to integer
        if(a == "recievedNewPatient"):
            # print("hereRPLrcv")
            self.checkCurrentPatientTemperature()


    def checkCurrentPatientTemperature(self):
        if self.currentPatient.getTemperature() > self.tempThreshold:
            print("in comparison")
            self.sense.set_pixels(Alarm())
            cond = True
            while cond:
                events = self.sense.stick.get_events()
                if events:
                    for event in events:
                        if event.action == 'pressed' and event.direction == 'middle':
                            print("pressed middle")
                            self.sense.clear()
                            cond = False
                            self.done = True
            
        
    def newPatient(self,patient):
        self.currentPatient = patient
        self.Format_and_Write("headquaters","time" "name:" + patient.getName() + "," +  "age:" + patient.getAge() + "," 
        + "gender:" + patient.getGender() + "," + "temperature:" + str(patient.getTemperature()))

    def closeAll(self):
        while self.close != 3:
            pass

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










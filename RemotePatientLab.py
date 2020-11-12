# COVID-19 Lab Simulation
# Remote Patient Lab
# date: Nov 12 2020
# name: Zoya Mushtaq
# description: Remote Patient Lab set up
class Patient

string Name
Integer Age
String Gender
Integer Temperature

#define setTemperature function
def setTemperature(temperature: Integer)
this.temperature=Temperature


#define getTemperature function
def getTemperature()
    Temperature = sense.get_temperature()

#define setName function
def setName(name: String)
this.name=Name

#define getName function
def getName()
return Name

#define setAge function
def setAge()
this.age=Age

#define getAge function
def getAge()
return Age 

#define setGender function
def setGender(gender: String)
this.gender=Gender

#define getGender function
def getGender()
return Gender

class RPL

String Name
Integer Age
Integer tempThreshold






class Thermal_Camera
Integer temperature

def setTemp(temp: Integer)
this.temp=temperature


def getTemp()
return temperature 

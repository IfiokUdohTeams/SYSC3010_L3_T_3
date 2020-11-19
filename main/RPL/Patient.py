# COVID-19 Lab Simulation
# Remote Patient Lab
# date: Nov 12 2020
# name: Zoya Mushtaq
# description: Remote Patient Lab set up
class Patient:

    def __init__(self,name,Age,gender):
        self.Name = name
        self.Age = Age
        self.Gender = gender
        self.Temperature = ""

    #define setTemperature function
    def setTemperature(self, Integer):
        self.Temperature = Integer


    #define getTemperature function
    def getTemperature(self):
        return self.Temperature


    #define getName function
    def getName(self):
        return self.Name

    #define getAge function
    def getAge(self):
        return self.Age 


    #define getGender function
    def getGender(self):
        return self.Gender
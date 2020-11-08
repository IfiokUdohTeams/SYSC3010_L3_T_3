End-to-End Source Documentation
This document contains important information for base classes used for communication between Node Type child Classes e.g.
Headquaters -> RemotePatientLab, RemotePatientLab -> Headquaters, RemoteVacineLab -> Headquaters etc.

Communicatioin Protocol
On initialization of a Node Object N, N polls the ThingSpeak Channel(TSC) used in its initialization, N recieves every message written to the TSC.Prior to initialization, TSC should be setup with 2 fields:
1. field1: sender_receiver, format: "sender" : sender, "receiver" : receiver, example: "sender" : headquaters, "receiver" : remotePatientLab
2. field2: data, format: depends on receiver format, example:"example"

N can also write to TSC specifying the reciever and data which wich must be formated to Ns specification based on Communication Protocol table.
NOTE: All nodes in the system should use the same TSC for communication to be possible

Contributing:
To contribute, clone repository and make your own branch

ToDo:
1.Fix bug to properly close threads reading from TSC
in the mean time developer can manually stop running process example:
unix-type OS:
sudo ps - ef | grep main.py     #or any python file that initializes Headquater, RemotePatientLab or RemoteVaccineLab Objects
sudo kill -9 num                #where num is  first group of unmbers after user 
example: ifiok    13376  2777 99 12:06 pts/0    00:00:45 python main.py 
user is ifiok therefore num = 13376 so to kill process, run: sudo kill -9 13376
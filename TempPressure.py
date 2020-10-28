#description: This code continially dipalys the temperature, humidity and pressure of
#a room on the sense hat LED board. 

from sense_hat import SenseHat #import vlaues from the sensehat to raspberry pi
import time #time helps me keep a log of all the vlues were measuring 
from time import asctime 

#assign the sense hat vlaues to a variable know as sense
sense = SenseHat()

class SenseHat:

	def read_Temperature():
		temp=round(sense.get_temperature()) #fxn get_temperature will give value measured by sense hat in degress celcuis whihc will be stored in temp variable 
		message = ' T=%dC ' %(temp) #store temp, with a specific notation in "message" string 
		sense.show_message(message, scroll_speed=(0.08), text_colour=[200,240,200], back_colour=[0, 0, 0]) #call in which i can send any message to my sense hat display screen. passing message string
		time.sleep(4) #this delays between each measurement 
		log = open('Temp.txt', "a") # i made a log file where i will write the present time and the temperature 
		now = str(asctime())
		log.write(now+''+message+'\n')
		print(message) #we will see the reading on the console by using this. now we will see it on the console and sense hat
		log.close()
		
	def read_Pressure(): 
		pressure = round(sense.get_pressure())   
		message2 = 'P=%d ' %(pressure) #store pressure,  with a specific notation in "message" string 
		sense.show_message(message2, scroll_speed=(0.08), text_colour=[200,240,200], back_colour=[0, 0, 0]) #call in which i can send any message to my sense hat display screen. passing message string
		time.sleep(4) #this delays between each measuremetn 
		log = open('Pressure.txt', "a") # i made a log file where i will write the present time and the pressure 
		now = str(asctime())
		log.write(now+''+message2+'\n')
		print(message2) #we will see the reading on the console by using this. now we will see it on the console and sense hat
		log.close()

	#infinate while loop that will continually meaure the temp, humidity, and pressure

	while True:
		read_Temperature()
		time.sleep(10) 
		read_Pressure()
		time.sleep(1800) #we  want to measure the temperature periodically every 30 minutes 

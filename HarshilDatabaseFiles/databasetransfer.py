from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3
import urllib.request
import requests
import threading
import random
import http.client
import random
from random import randint
import string


get_data = requests.get('https://api.thingspeak.com/channels/1154762/feeds.json?api_key=8K3AMSEX1O5KUUPD&results').json()



#connect to database file
dbconnect = sqlite3.connect("VaccinePatientDatabase.db");

#access columns
dbconnect.row_factory = sqlite3.Row;

#create cursor to work with db
cursor = dbconnect.cursor();
cursor2 = dbconnect.cursor();


field_2 = get_data['feeds']

lab1 =[]
for x in field_2:
    lab1.append(x['field2'])
    


lab2 =[]
for y in field_2:
    lab2.append(y['field2'])
    


patient =[]
for z in field_2:
    patient.append(z['field2'])
    


#store all values in SQL database
for i in lab1:
    temp = i+chr(176)
    press = i+chr(80)+chr(97)
    cursor.execute('''INSERT INTO lab1 VALUES (?,?)''',(temp,press));
    dbconnect.commit();
    
for j in lab2:
    temp2 = j+chr(176)
    press2 = j+chr(80)+chr(97)
    cursor.execute('''INSERT INTO lab2 VALUES (?,?)''',(temp2,press2));
    dbconnect.commit();
    
for k in patient:
    ptemp = k+chr(176)
    pname = random.choice(string.ascii_letters)
    page = randint(20,80)
    cursor.execute('''INSERT INTO patient VALUES (?,?,?)''',(pname,page,ptemp));
    dbconnect.commit();
    

# #clear Databases
# cursor.execute('DELETE FROM lab1');
# dbconnect.commit()
# cursor.execute('DELETE FROM lab2');
# dbconnect.commit()
# cursor.execute('DELETE FROM patient');
# dbconnect.commit()  






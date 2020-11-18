import sqlite3
import CreateDatabase



dbconnect = sqlite3.connect("P.db");
cursor = dbconnect.cursor();
db = cursor.execute('''CREATE TABLE IF NOT EXISTS P(Name TEXT, Age NUMERIC, Gender TEXT, Temperature NUMERIC, Threshold NUMERIC)''');


def insertData(Name, Age, Gender, Temperature, Threshold):
    cursor.execute('''INSERT INTO P (Name, Age, Gender, Temperature, Threshold) VALUES (?, ?, ?, ?, ?)''', (Name, Age, Gender, Temperature, Threshold))
    dbconnect.commit()

def insertThreshold(Threshold):
    cursor.execute('''INSERT INTO P (Threshold) VALUES (?)''', (Threshold))
    dbconnect.commit()
    
def getInfo():
    cursor.execute('SELECT Name, Age, Gender FROM P');
    records = cursor.fetchall()
    print records
    
def getTempbyName(Name):
    cursor.execute('SELECT Temperature FROM P WHERE Name = Name');
    records = cursor.fetchall()
    print records
        
def getTemp():
    cursor.execute('SELECT Temperature FROM P');
    records = cursor.fetchall()
    print records
        
def getThreshold():
    cursor.execute('SELECT Threshold FROM P');
    records = cursor.fetchall()
    print records    
        

    
dbconnect.commit;
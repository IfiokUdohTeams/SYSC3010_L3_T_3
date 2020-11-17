import sqlite3
import CreateDatabase



dbconnect = sqlite3.connect("V2.db");
cursor = dbconnect.cursor();
db = cursor.execute('''CREATE TABLE IF NOT EXISTS V2(Temperature NUMERIC, TempT NUMERIC, Pressure NUMERIC, PresT NUMERIC)''');


def insertData(Temp,  Pressure, TempT, PresT):
    t = Temp
    p = Pressure
    cursor.execute('''INSERT INTO V2 (Temperature, TempT, Pressure, PresT) VALUES (?, ?,?,?)''', (t, p,TempT, PresT))
    dbconnect.commit()

def insertThreshold(Temp,  Pressure):
    t = Temp
    p = Pressure
    cursor.execute('''INSERT INTO V2 (TempT, PresT) VALUES (?, ?)''', (t, p))
    dbconnect.commit()
    
def getTemp():
    cursor.execute('SELECT Temperature FROM V2');
    records = cursor.fetchall()
    print records
    
def getPres():
    cursor.execute('SELECT Pressure FROM V2');
    records = cursor.fetchall()
    print records
        
def getTempT():
    cursor.execute('SELECT TempT FROM V2');
    records = cursor.fetchall()
    print records
        
def getPresT():
    cursor.execute('SELECT PresT FROM V2');
    records = cursor.fetchall()
    print records    
        

    
dbconnect.commit;
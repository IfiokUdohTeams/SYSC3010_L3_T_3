import Headquaters
import RemotePatientLab
import RemoteVaccineLab


def main():
    TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
    readKey = '0'
    writeKey = "OEGCYO9F8FJCZGO6"
    hq = Headquaters.Headquaters(TSC,readKey, writeKey)
    rpl = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)
    writeData = "testing1"
    readData = ""
    hq.Format_and_Write(hq.node_id, writeData)

    while(readData == ""):
        readData = hq.getReadBack()
        
    hq.readBackDiscard()
    print("Test result:", writeData == readData)
    hq.close()
    rpl.close()
    # hq.Format_and_Write(rpl.node_id, "testing2")

if __name__ == '__main__':
    #Add code with nodes, use every time to handle stopping all running processes
    # signal.signal(signal.SIGINT, signal_handler)
    #code with node
    main()
    # signal.pause()
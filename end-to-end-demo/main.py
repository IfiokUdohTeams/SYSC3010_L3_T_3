import Headquaters
import RemotePatientLab
import RemoteVaccineLab
import signal
import sys

def signal_handler(sig, frame):
    print('Stopped all Processes reading from TSC')
    sys.exit(0)

def main():
    TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
    readKey = '0'
    writeKey = "OEGCYO9F8FJCZGO6"
    hq = Headquaters.Headquaters(TSC,readKey, writeKey)
    rpl = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)


    hq.Format_and_Write(hq.node_id, "testing1")
    # hq.Format_and_Write(rpl.node_id, "testing2")

if __name__ == '__main__':
    #Add code with nodes, use every time to handle stopping all running processes
    # signal.signal(signal.SIGINT, signal_handler)
    #code with node
    main()
    # signal.pause()
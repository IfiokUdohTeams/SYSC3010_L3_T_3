import time
import sys
import signal
sys.path.append('..')
from RPL import RemotePatientLab

def main():
        # Initialize nodes in communication path
    TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
    readKey = '0'
    writeKey = "OEGCYO9F8FJCZGO6"

    
    remotepatientLab = RemotePatientLab.RemotePatientLab(TSC,readKey, writeKey)
    remotepatientLab.tempThreshold = 30

    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        remotepatientLab.closeAll()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')
    signal.pause()

if __name__ == "__main__":
    main()
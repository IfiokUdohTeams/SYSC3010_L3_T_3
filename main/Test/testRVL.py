import time
import sys
import signal
sys.path.append('..')
from RVL import RemoteVaccineLab

def main():
        # Initialize nodes in communication path
    TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
    readKey = '0'
    writeKey = "OEGCYO9F8FJCZGO6"

    print('type done, Press Enter then Press Ctrl+C to exit Program')
    remoteVaccineLab = RemoteVaccineLab.RemoteVaccineLab(TSC,readKey, writeKey)
    # remoteVaccineLab.ConnectToAndroidApp()
    # remotepatientLab.tempThreshold = 30

    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        remoteVaccineLab.closeAll()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

if __name__ == "__main__":
    main()
import time
import sys
import signal
sys.path.append('..')
from Headquaters import Headquaters



def main():
        # Initialize nodes in communication path
    TSC = 'https://api.thingspeak.com/channels/1161330/feeds.json?'
    readKey = '0'
    writeKey = "OEGCYO9F8FJCZGO6"
    host = "192.168.0.57"
  
    headquaters = Headquaters.Headquaters(TSC,readKey, writeKey, host)
    headquaters.ConnectToAndroidApp()
    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        headquaters.closeAll()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit Program')
    signal.pause()

if __name__ == "__main__":
    main()
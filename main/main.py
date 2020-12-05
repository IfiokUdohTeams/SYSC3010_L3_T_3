'''
main.py initializes and runs system based off pareameters in config.txt
Authors: Ifiok Udoh

'''
import sys
import signal
import ConfigProcessor
from Headquaters import Headquaters
from RVL import RemoteVaccineLab
from RPL import RemotePatientLab

def main():
    config = ConfigProcessor.ConfigProcessor()
    # print(config.node)
    if config.node == 'headquaters':
        headquaters = Headquaters.Headquaters(config.TSC,config.readKey, config.writeKey, config.AndroidAppIpAddress)
        headquaters.ConnectToAndroidApp()
        def signal_handler(sig, frame):
            print('You pressed Ctrl+C!')
            headquaters.closeAll()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit Program')
        signal.pause()
    
    elif config.node == 'remoteVaccineLab':
        remoteVaccineLab = RemoteVaccineLab.RemoteVaccineLab(config.TSC,config.readKey, config.writeKey,
         config.node+config.RemoteVaccineLabNo, config.AndroidAppIpAddress, config.RemoteVaccineLabPollTime, config.sense)
        remoteVaccineLab.ConnectToAndroidApp()
        def signal_handler(sig, frame):
            print('You pressed Ctrl+C!')
            remoteVaccineLab.closeAll()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit Program')
        signal.pause()

    elif config.node == 'remotePatientLab':
        remotepatientLab = RemotePatientLab.RemotePatientLab(config.TSC,config.readKey, config.writeKey, config.sense)

        def signal_handler(sig, frame):
            print('You pressed Ctrl+C!')
            remotepatientLab.closeAll()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit Program')
        signal.pause()

if __name__ == "__main__":
    main()

'''
Authors: Ifiok Udoh

'''
class ConfigProcessor:
    def __init__(self):
        self.configFile                 = "config.txt" #config file
        self.node                       = None
        self.RemoteVaccineLabNo         = None
        self.AndroidAppIpAddress        = None
        self.RemoteVaccineLabPollTime   = None
        self.TSC                        = None
        self.readKey                    = None
        self.writeKey                   = None
        self.sense                      = None
        self.process()

    def process(self):
        f = open(self.configFile, 'r')
        raw = str(f.read())
        raw = raw.strip().split('\n')
        for i in raw:
            if i != '':
                line = i.split(';')[0].replace(" ", "")
                slitline = line.split("=")
                key = slitline[0]
                value = slitline[1]
                if key == "Node":
                    self.node = value
                elif key == "RemoteVaccineLabNo":
                    self.RemoteVaccineLabNo = value
                elif  key == "AndroidAppIpAddress":
                    self.AndroidAppIpAddress = value
                elif  key == "RemoteVaccineLabPollTime":
                    self.RemoteVaccineLabPollTime = float(value)
                elif  key == "ThingSpeakChannel":
                    self.TSC = value
                elif  key == "readKey":
                    self.readKey = value
                elif  key == "writeKey":
                    self.writeKey = value
                elif  key == "sense":
                    self.sense = value
                

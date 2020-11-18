import sys
sys.path.append('..')
from Communication import Node

class RemotePatientLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(RemotePatientLab, self).__init__(thingSpeak_url, readKey, writeKey,"remotePatientLab")
        self.ReadList = []

    # def FormatData(self,data):

    def process_data(self):
        # print("remotePatientLab READ: ", self.read_data_pointer[0], " from: ", self.read_sender_pointer[0])
        a =  self.read_data_pointer[0]
        self.ReadList.append(int(a.encode("ascii"))) # encode read unicode string to ascii and convert to integer
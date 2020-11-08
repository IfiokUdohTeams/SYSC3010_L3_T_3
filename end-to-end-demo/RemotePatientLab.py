import Node

class RemotePatientLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(RemotePatientLab, self).__init__(thingSpeak_url, readKey, writeKey,"remotePatientLab")

    # def FormatData(self,data):

    def process_data(self):
        print("remotePatientLab READ: ", self.read_data_pointer[0], " from: ", self.read_sender_pointer[0])
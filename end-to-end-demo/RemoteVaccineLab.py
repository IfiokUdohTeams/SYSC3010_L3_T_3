import Node

class RemoteVaccineLab(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(RemoteVaccineLab, self).__init__(thingSpeak_url, readKey, writeKey,"remoteVaccineLab")

    # def FormatData(self,data):


    def process_data(self):
        print("remoteVaccineLab READ: ", self.read_data_pointer[0], " from: " ,self.read_sender_pointer[0])
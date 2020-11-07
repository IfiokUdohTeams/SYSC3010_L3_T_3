import Node

class Headquaters(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(Headquaters, self).__init__(thingSpeak_url, readKey, writeKey,"headquaters")

    # def FormatData(self,data):

    def process_data(self):
        print("headquaters READ: ", self.read_data_pointer[0], " from: ", self.read_sender_pointer[0])
import Node

class Headquaters(Node.Node):
    def __init__(self, thingSpeak_url, readKey, writeKey):
        super(Headquaters, self).__init__(thingSpeak_url, readKey, writeKey,"headquaters")
        self.ReadList = []

    # def FormatData(self,data):

    def process_data(self):
        # print("headquaters READ: ", self.read_data_pointer[0].encode("ascii"), " from: ", self.read_sender_pointer[0])
        a =  self.read_data_pointer[0]
        self.ReadList.append(int(a.encode("ascii"))) # encode read unicode string to ascii and convert to integer

    

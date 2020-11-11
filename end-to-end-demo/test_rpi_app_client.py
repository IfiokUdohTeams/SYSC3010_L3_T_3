import socket
import unittest

class Test_rpi_app_client(unittest.TestCase):

    def test_app_client(self):
        host = socket.gethostname()  # as both code is running on same pc
        host = '192.168.0.52'
        port = 8080  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        recvList = ""
        cond = True
        while(cond):
            data = client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            recvList = data
            cond = False

        client_socket.close()  # close the connection
        recvList = recvList.encode("ascii").split(", ")
        data = []
        for i in recvList:
            data.append(int(i))
        
        self.assertEqual(data, [1,12, 45])


if __name__ == '__main__':
    unittest.main()
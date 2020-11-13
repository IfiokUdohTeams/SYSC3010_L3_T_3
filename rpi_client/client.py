import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    host = '192.168.0.52'
    port = 8080  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = raw_input(" -> ")  # take input
    message = message + "\n"

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        # client_socket.flush()
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = raw_input(" -> ")  # again take input
        message = message + "\n"

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
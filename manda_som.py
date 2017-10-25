import socket
import sys


class SendText():
    def __init__(self):
        self.porta = 3656
        
    def send_socket(self, texto):    
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self.porta)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)

        try:
            # Send data
            texto = texto + '&'         
            message = texto.encode()
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            # amount_received = 0
            # amount_expected = len(message)

            # while amount_received < amount_expected:
            #     data = sock.recv(16)
            #     amount_received += len(data)
            #     print('received {!r}'.format(data))

        finally:
            print('closing socket')
            sock.close()

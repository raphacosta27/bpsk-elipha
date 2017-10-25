# Camada Física da Computação
# Exemplo socket server
## https://pymotw.com/2/socket/tcp.html

import socket
import sys

class TextGetter():
    def __init__(self, porta):
        self.porta = porta
        self.aberto = False

    def initialize_socket(self):

        print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        self.server_address = ('localhost', self.porta)
        print("PORTA {}".format(self.porta))
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)
        while True:
                print("waiting for a connection")
                self.connection, self.client_address = self.sock.accept()
                print(" connection from {}".format(self.client_address))
                break
        self.aberto = True

    def getText(self):   
        if self.aberto == False:
            return "Abra o Socket"
        else:    
            # Receive the data in small chunks and retransmit it
            while True:
                data = self.connection.recv(16)
                print(len(data))
                # if str(data, 'utf-8') == '&':
                #     print("é &")
                #     return '&'
                print("{}".format(str(data, 'utf-8')), end="")
                if len(data) > 0:
                    # print("{}".format(str(data, 'utf-8')), end="")
                    return str(data, 'utf-8')
                if len(data) == 0:
                    print("vazio")

                if(len(data) <= 0):
                    print("é o prezo")
                    break
            print("alo")
        # self.close_socket()
        # except UnicodeDecodeError:
        #     pass
    def close_socket(self):
        self.aberto = False
        print("Fechou socket")
        self.sock.close()
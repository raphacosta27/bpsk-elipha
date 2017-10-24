# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys

def initialize_socket(porta):
    PORTA = porta

    print("Inicializando socket TCP/IP")
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', PORTA)
    print("PORTA {}".format(PORTA))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()

        try:
            print(" connection from {}".format(client_address))

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                if len(data) > 0:
                    print("{}".format(str(data, 'utf-8')), end="")
                if(len(data) <= 0):
                    break

        finally:
            # Clean up the connection
            connection.close()
    
def main():
    initialize_socket(1234)

if __name__ == "__main__":
    main()
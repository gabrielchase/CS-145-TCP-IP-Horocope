from __future__ import print_function

import socket
import time

# Create a UDP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
serversocket.bind(server_address)

if __name__ == "__main__":
    while True:
        print('\nwaiting to receive message')
        start = time.time()
        data, address = serversocket.recvfrom(4096)
        print("Received ", data)

        if data:
            print("Sending: ", data)
            sent = serversocket.sendto(data, address)
            
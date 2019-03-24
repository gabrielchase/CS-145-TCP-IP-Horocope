from __future__ import print_function

import socket
import time

# Create a UDP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

if __name__ == "__main__":
    for i in range(1, 4):
        # Send data
        start_time = time.time()
        send_data = '{}'.format(i).encode()
        sent = clientsocket.sendto(send_data, server_address)

        # Receive response
        received_data, server = clientsocket.recvfrom(4096)
        received_data = received_data.decode()
        print("Received: ", received_data)
        if received_data == str(i):
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 1:
                print("LOST")
            else:
                print("Completed in: ", elapsed_time)

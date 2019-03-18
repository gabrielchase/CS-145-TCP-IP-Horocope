from __future__ import print_function

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("127.0.0.1", 58917))

if __name__ == "__main__":
    while (True):
        user_input = raw_input("Input a date: ")
        if (user_input == "q"):
            # close connection
            break
        else:
            clientsocket.send(user_input.encode())
            response = clientsocket.recv(1024).decode()
            print(response)

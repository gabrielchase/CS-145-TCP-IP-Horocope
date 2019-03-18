import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("127.0.0.1", 58916))

if __name__ == "__main__":
    while (True):
        user_input = input("Input a date: ")
        if (user_input == "q"):
            break
        else:
            clientsocket.send(user_input.encode())
            response = clientsocket.recv(1024).decode()
            print(response)

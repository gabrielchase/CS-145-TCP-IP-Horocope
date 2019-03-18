import math
import socket
import json 

HOROSCOPES_JSON = []

with open('HOROSCOPE.json') as f:
    HOROSCOPES_JSON = json.load(f)

ZELLERS_MONTH = {
    "March": 1,
    "April": 2,
    "May": 3,
    "June": 4,
    "July": 5,
    "August": 6,
    "September": 7,
    "October": 8,
    "November": 9,
    "December": 10,
    "January": 11,
    "February": 12,
}

ZELLERS_DAY = {
    "0": "Sunday",
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
}

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 58916))
serversocket.listen(5) # become a server socket, maximum 5 connections

# Zeller's Rule
def zellers_rule(K, M, D, C):
    if (M == 11 or M == 12):
        D = D - 1
    F = K + math.floor((13 * M -1) / 5) + D + math.floor(D/4) + math.floor(C/4) - math.floor(2*C)
    F = str(math.floor(F % 7))
    return ZELLERS_DAY[F]

def get_day_of_the_week(date):
    month, day, year = date.split()
    K = float(day)
    M = ZELLERS_MONTH[month]
    D = float(year[2:4])
    C = float(year[0:2])
    return zellers_rule(K, M, D, C)

def get_horoscope(date):
    month, day, year = date.split()
    for counter, value in enumerate(HOROSCOPES_JSON):
        value = json.loads(json.dumps(value))
        if value["start"]["month"] == month:
            if value["start"]["day"] <= int(day):
                return value 
            else:
                return HOROSCOPES_JSON[counter-1]

while True:
    client_socket, address = serversocket.accept()
    while True:
        data = client_socket.recv(1024).decode()
        print("Received: ", data)
        
        day_of_the_week = get_day_of_the_week(data)
        horoscope = get_horoscope(data)
        
        result = '{};{};{}'.format(day_of_the_week, horoscope["symbol"], horoscope["reading"])
        print(result)
        client_socket.send(result.encode())

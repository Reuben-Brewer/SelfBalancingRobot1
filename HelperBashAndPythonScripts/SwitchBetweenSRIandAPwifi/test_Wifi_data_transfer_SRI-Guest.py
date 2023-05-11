import socket
import time

#HOST = "192.168.4.1" #ReubenPiNetwork1
HOST = "10.255.254.20"
PORT = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
     data, addr = s.recvfrom(1024)
     print data


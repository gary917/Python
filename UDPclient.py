#Client side
from socket import *
import time;

serverName = '192.168.0.42'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input('Send a message: ')
clientSocket.sendto (message.encode(),(serverName, serverPort))
#record current time when packet is sent to server
start_time = time.time()
message, serverAddress = clientSocket.recvfrom(2048)
#calculate time difference when message received
elapsed_time = time.time() - start_time
print("Received Message : %s" %message.decode())
print("*********")
print("Calculated RTT is %lf seconds" %elapsed_time)
print("*********")


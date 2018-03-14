#Server side
from socket import *

serverName = '192.168.0.41'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is read to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
#	gets the message and echoes it	
	echoMessage = message.decode()
	serverSocket.sendto(echoMessage.encode(), clientAddress)
	print("Message echoed")

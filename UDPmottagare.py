# UDP Mottagare
from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")
lastNum = 10000 
while True:
    # read client's message and remember client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)

    payload = message.decode()
    msgNum = int(payload[:5])
    # Print message and client address
    print ("Packet nr: ", msgNum  , lastNum)
    
    lastNum2 = msgNum - 1
    if(lastNum != lastNum2 and msgNum != 0):
        print ("log: felaktig ordning", lastNum, "=>", msgNum)
    lastNum = int(payload[:5])    
    print (clientAddress)
    
    # change sentence to upper case letters
    #modifiedMessage = message.decode().upper()
    
    # send back modified sentence to client using remembered address
    #serverSocket.sendto(modifiedMessage.encode(), clientAddress)


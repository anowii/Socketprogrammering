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
    # Print packet nr
    print ("Packet nr: ", msgNum)
    
    lastNum2 = msgNum - 1
    # if the (current packaged number -1) != (the last package number) the packages are in disorder.
    if(lastNum != lastNum2):
        print ("log: felaktig ordning", lastNum, "=>", msgNum)
    # saves the current package number
    lastNum = int(payload[:5])    
    #Print client address 
    print (clientAddress)

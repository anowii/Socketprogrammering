# TCP Mottagare
from socket import *
serverPort = 12000
lastNum = 10000

# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

# server starts listening for incoming TCP requests
serverSocket.listen(1)

print ('The TCP server is ready to receive')
# server waits for incoming requests; new socket created on return
connectionSocket, addr = serverSocket.accept()
while True:
    # read payload of bytes from socket sent by the client
    payload = connectionSocket.recv(1500).decode()
    msgNum = int(payload[:5])
    # print package number 
    print ("Packet nr: ", msgNum)

    # if the (current packaged number -1) != (the last package number) the packages are in disorder.
    lastNum2 = msgNum - 1
    if(lastNum != lastNum2 and msgNum != 0):
        print ("log: felaktig ordning", lastNum, "=>", msgNum)
    # saves the current package number
    lastNum = int(payload[:5])    
    # print client address
    print (addr)

# close the TCP connection; the welcoming socket continues
connectionSocket.close()

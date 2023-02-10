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
    print ("Packet nr: ", msgNum  , lastNum)

    lastNum2 = msgNum - 1
    if(lastNum != lastNum2 and msgNum != 0):
        print ("log: felaktig ordning", lastNum, "=>", msgNum)
    lastNum = int(payload[:5])    
    print (addr)

#close the TCP connection; the welcoming socket continues
connectionSocket.close()

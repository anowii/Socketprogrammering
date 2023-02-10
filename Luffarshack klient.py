# TCP Client program från exempel del A
# Anders Nelsson BTH
# Exempel från kursbok

from socket import *
import os
# serverName = 'hostname'
serverName = 'www.ingonline.nu'
serverPort = 80

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# GET - message request
request = 'GET /tictactoe/index.php?board=xoxoxoeex HTTP/1.1\r\nHost:www.ingonline.nu\r\n\r\n'

# send text over the TCP connectionS
# there's no need to specify server name & port
# sentence converted to bytes
clientSocket.send(request.encode())


# get response back from server
response = clientSocket.recv(1024).decode()
print ('From weberver:\n', response)


# close the TCP connection
clientSocket.close()

#added so i can see the response from the webserver
os.system("pause")

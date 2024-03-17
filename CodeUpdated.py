#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12005
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print("The server is running")
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept() 
    #Fill in end
    print('This part works')
    try:
        #Fill in start 
        message = connectionSocket.recv(1024).decode()
        print(message)
        #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start    
        outputdata = f.read()
        #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        header = 'HTTP/1.1 200 OK\n'
        header.encode()
        connectionSocket.send(header)
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (This Should be a 404 File Not Found Page?)
        #Fill in start
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Netfun Webserver</p></center></body></html>'
        header += response
        connectionSocket.send(header.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
    serverSocket.close()
    exit() #Terminate the program after sending the corresponding data

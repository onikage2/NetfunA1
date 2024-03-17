from socket import * #Imports the socket module
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12005
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("The server is running")
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        print("Opening: " + filename[1:])
        f = open(filename[1:])   
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\n\n'
        #for i in range(0, len(outputdata)):
            #print(header + outputdata[i])
            #connectionSocket.send((header + outputdata[i]).encode())
        #connectionSocket.send("\r\n".encode())
        print("Sending Data: " + header + outputdata)
        connectionSocket.send((header + outputdata).encode())
        connectionSocket.close()
    except IOError:
        print("IO ERROR")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><meta charset="UTF-8"><body><center><h1>Error 404: File not found</h1><p>Netfun Webserver</p><p><div style="font-size:5rem;width:100%;text-align:center;">&#x1F928;</div></p></center></body></html>'
        header += response
        print(header)
        connectionSocket.send(header.encode())
        connectionSocket.close()
serverSocket.close()
exit() #Terminates the program (However will not occur as program runs forever)

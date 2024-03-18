from socket import * #Imports the socket module
serverSocket = socket(AF_INET, SOCK_STREAM) #Initialises a socket object
serverPort = 12123 #Denote the chosen port number
serverSocket.bind(('', serverPort)) #Binds the serverSocket object to the specified port on the line above
serverSocket.listen(1) #Tells the Program to keep the connection by denoting "1"
print("The server is running")
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode() #Recieves and decodes a message from the connection socket
        filename = message.split()[1] #Splits the message to get just the file path
        print("Opening: " + filename[1:])
        f = open(filename[1:], errors="ignore") #Denotes f as the open file ignoring the initial /
        outputdata = f.read() #Reads the data in the file and places into outputdata
        header = 'HTTP/1.1 200 OK\n\n'
        print("Sending Data: " + header + outputdata)
        connectionSocket.send((header + outputdata).encode()) #Encodes and then sends the HTML data through the socket
        connectionSocket.close() #Closes the current connection however continues to listen
    except IOError: #Uses the try line to look for errors, if they occur are caught by the except line, IOError looks for errors concerning file accessing
        print("IO ERROR")
        outgoingm = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><meta charset="UTF-8"><body><center><h1>Error 404: File not found</h1><p>Networking Project</p><p><div style="font-size:5rem;width:100%;text-align:center;">&#x1F928;</div></p></center></body></html>'
        outgoingm += response
        connectionSocket.send(outgoingm.encode()) #Endoces and sends the HTML line containing the data for the browser to display to the user
        connectionSocket.close()
    except:
        print("Unexplained Error")
        connectionSocket.close()
serverSocket.close() #Stops the connection through the socket
exit() #Terminates the program (However will not occur as program runs forever while True)

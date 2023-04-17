from socket import *



# set server port
serverPort = 12000

# create server socket and bind to port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# listen for incoming connections
serverSocket.listen(1)

# print message to indicate that server is ready
print('The server is ready to receive')

while True:
    # accept incoming connection
    connectionSocket, addr = serverSocket.accept()

    # receive data from client and convert to uppercase
    sentence = connectionSocket.recv(1024).decode()
    #capitalizedSentence = sentence.upper()

    if sentence == "hehe":
        reply = "kau dah kenapa"
        connectionSocket.send(reply.encode())

    #print the message
    print("Message: " ,  sentence)

    # send modified data back to client
    connectionSocket.send(sentence.encode())


    #The error TypeError: a bytes-like object is required, not 'str' occurs because the send() method of the connectionSocket object expects a bytes-like object as its argument, but you are passing a string object instead.
    #In Python 3.x, strings are Unicode by default, whereas network sockets communicate using bytes. So, you need to convert the string to bytes before sending it over the socket.


    # close connection socket
    connectionSocket.close()


#The print statement has been updated to use parentheses to make it a function call, which is the recommended style in Python 3.
#The while loop has been modified to use True instead of 1.
#The connectionSocket.recv() method returns a bytes object in Python 3, so we don't need to call decode() on it like we did in Python 2.
#I added comments to explain what each section of the code does.
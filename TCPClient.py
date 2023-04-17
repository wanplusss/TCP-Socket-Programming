#this is for tcpClient built using Python 3.10
from socket import *

user_input = ""



#loop:


while user_input == "":
        # set server name and port
    serverName = '172.16.72.65' #need to put new servername based on current ip since it can give dhcp sometimes
    serverPort = 12000

    # create client socket and connect to server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # get user input and send to servern
    sentence = input('Input lowercase sentence: ').encode()
    clientSocket.send(sentence)

    # receive response from server and print it
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())

    user_input = input("Do you still want to continue? : ")


# close the client socket
clientSocket.close()


#added comments by chatGPT

#The code is very similar to the previous version for Python 3, with just a few minor changes:

#I added comments to explain what each section of the code does.
#I updated the print statement to use parentheses to make it a function call, which is the recommended style in Python 3.
#I used the encode() method to convert the user input to bytes before sending it over the socket.
#I used the decode() method to convert the bytes received from the server back into a string before printing it.
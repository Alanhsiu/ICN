from socket import *

# Note: After finishing the program, try to type http://HOST:PORT/index.html in your browser for test

ServerSocket = socket(AF_INET, SOCK_STREAM, proto=0)
# Create a socket and bind the socket to the address
# TODO start
HOST, PORT = "127.0.0.1", 2089
# HOST, PORT = ServerSocket.getsockname()[0], 2089
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
# TODO end

while True:
    print('Ready to serve...')

    # Establish the connection
    # TODO start
    ConnectionSocket, Addr = serverSocket.accept()
    print(str(Addr)+"connected")
    # TODO end

    try:
        # Receive a HTTP request from the client
        # TODO start
        RecvMessage = ConnectionSocket.recv(2048).decode()
        print(RecvMessage)
        # TODO end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]
        print(FileName)
        f = open(FileName[1:], encoding='utf-8')

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # TODO start
        DataInFile = f.readlines()
        f.close()
        # TODO end 

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # TODO start
        ConnectionSocket.send(b'HTTP/1.1 200 OK\r\n')
        # TODO end

        # Send the Content Type to the client
        # TODO start
        ConnectionSocket.send(b'Content-Type: text/html; charset=utf-8\r\n\r\n') 
        # TODO end

        # Send the content of the requested file to the client
        for i in range(len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send(b"\r\n")

        ConnectionSocket.close()
    except IOError:
        # Send the response message if the file is not found
        # TODO start
        res = "404 Not Found"
        ConnectionSocket.send((res+"\r\n").encode())
        # ConnectionSocket.send(b"\r\n")
        print(res)
        # TODO end

        # Close client socket
        # TODO start
        ConnectionSocket.close()
        # TODO end


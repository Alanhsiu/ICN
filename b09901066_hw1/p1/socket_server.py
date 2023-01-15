from socket import *
from datetime import datetime
from numpy import double
import math
import time

with open('./server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address 
    # TODO start
    HOST, PORT = "127.0.0.1", 2089
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    print("The server is ready to receive.")
    # TODO end

    while True:
        # Listen to any request
        # TODO start
        serverSocket.listen(1)
        # TODO end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        while True:
            try:
                # Accept a new request
                # TODO start
                Client, Addr = serverSocket.accept()
                # TODO end

                while True:
                    Client.send(b"Please input a question for calculation")
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # TODO start
                    sentence = Client.recv(1024).decode()
                    res = sentence.split()
                    ans = -1
                    print("client message is:", res[1])
                    print(res[1])
                    if (res[1] == '+'):
                        ans = double(res[0])+double(res[2])
                    elif (res[1] == '-'):
                        ans = double(res[0])-double(res[2])
                    elif (res[1] == '*'):
                        ans = double(res[0])*double(res[2])
                    elif (res[1] == '/'):
                        ans = double(res[0])/double(res[2])
                    # elif (res[1] == '^'):
                    #     # ans = math.pow(int(res[0]),int(res[2]))
                    #     temp = 1
                    #     for i in range(int(res[2])):
                    #         temp *= int(res[0])
                    #     ans = temp
                    # elif (res[0] == 'gcd'):
                    #     m = max(int(res[1]), int(res[2]))
                    #     n = min(int(res[1]), int(res[2]))
                    #     r = m % n
                    #     while r != 0:
                    #         m = n
                    #         n = r
                    #         r = m % n
                    #     ans = n
                    # elif (res[0] == 'lcm'):
                    #     m = max(int(res[1]), int(res[2]))
                    #     n = min(int(res[1]), int(res[2]))
                    #     r = m % n
                    #     while r != 0:
                    #         m = n
                    #         n = r
                    #         r = m % n
                    #     ans = int(res[1])*int(res[2])/n
                    # elif (res[1] == 'dot'):
                    #     v1 = res[0].split(',')
                    #     v2 = res[2].split(',')
                    #     temp = 0
                    #     for i in range(len(v1)):
                    #         temp += double(v1[i])*double(v2[i])
                    #     ans = temp
                    # elif (res[0] == 'dist'):
                    #     p = res[1].split(',')
                    #     q = res[2].split(',')
                    #     x = double(p[0])-double(q[0])
                    #     y = double(p[1])-double(q[1])
                    #     ans = math.pow(x*x+y*y,0.5)

                    print("the ans is:", ans)
                    strAns = str(ans)
                    Client.send(strAns.encode())
                    Client.send(b"\nDo you wish to continue? (Y/N)")
                    sentence = Client.recv(1024).decode()
                    print("client message is:", sentence)
                    if (sentence == "N"):
                        break
                    # TODO end
                break
            except ValueError:
                continue
        break
    logFile.close()
    # Close the socket
    # TODO start
    Client.close()
    # TODO end

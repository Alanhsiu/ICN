from socket import *
import time

with open('./b09901066_p1_client_result.log', 'w') as logFile:
    logFile.write("The Client is running..\n")
    logFile.flush()

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # TODO start
    HOST, PORT = "127.0.0.1", 2089
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    # TODO end

    Testcase = open('./p1_testcase', 'r')
    TestcaseContents = Testcase.readlines()
    Testcase.close()

    # Write the information of HOST and PORT to the client_log.txt 
    # TODO start
    logFile.write("Connect to ")
    logFile.write(HOST)
    logFile.write(", using port number ")
    logFile.write(str(PORT))
    logFile.write("\n")
    logFile.flush()
    # TODO end

    # Read test cases from p1_testcase
    # You can change the test case or create other test cases on your own
    listSize = len(TestcaseContents)
    for idx in range(0,listSize,2):

        sentence = clientSocket.recv(1024)
        print('From Server:', sentence.decode())

        logFile.write("Received the message from server: ")
        logFile.write(sentence.decode())
        logFile.write("\n")

        # For connection stability
        time.sleep(3)

        # Client sent the request to the server and receive the response from the server
        # TODO start

        # get the question from server
        Line = TestcaseContents[idx].strip()
        print(Line)
        clientSocket.send(Line.encode())
        logFile.write("Question: ")
        logFile.write(Line)
        logFile.write("\n")

        # get the ans from server
        ans = clientSocket.recv(1024)
        print('Ans is:', ans.decode())
        logFile.write("Answer: ")
        logFile.write(ans.decode())
        logFile.write("\n")
        # question = clientSocket.recv(1024)
        # print('From Server:', question.decode())
        # logFile.write(sentence.decode())
        # logFile.write("\n")
        # logFile.flush()
        Line1 = TestcaseContents[idx+1].strip()
        print(Line1)
        logFile.write(Line1)
        logFile.write("\n")
        time.sleep(3)
        clientSocket.send(Line1.encode())
        # TODO end

    # Close the socket
    # TODO start
    clientSocket.close()
    # TODO end
logFile.close()

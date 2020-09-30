from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScop
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <a@a.com>\r\n.'
    clientSocket.send(mailfromCommand.encode())
    recv1 = clientSocket.recv(1024)
   #print(recv1)
  
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO: <a@a.com>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)
  
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'Data'
    #print(dataCommand)
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    # Fill in end

    # Send message data.
    # Fill in start
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
   # print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024)
    clientSocket.close()
    #print(recv1) 
    
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')


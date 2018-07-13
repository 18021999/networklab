import socket
UDP_IP_ADDRESS="10.1.24.137"
UDP_PORT_NUMBER=6750
Message=("Hello Server")
bytesToSend = str.encode(Message)
clientSock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend ,(UDP_IP_ADDRESS,UDP_PORT_NUMBER))  
messagefromserver=clientSock.recvfrom(1024)
print(messagefromserver)

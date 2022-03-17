import socket
localIP     = "localhost"
localPort   = 9999
bufferSize  = 1024
msgFromServer       = "Hello client"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Bạn đã nhận được tin nhắn từ client :{}".format(message)
    clientIP  = "Địa chỉ ip của client :{}".format(address)
    print(clientMsg)
    print(clientIP)
    UDPServerSocket.sendto(bytesToSend, address)

import socket

host = 'localhost'
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
print('đã kết nối đến cổng', port)

while(True):
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Bạn đã nhận được tin nhắn từ client :{}".format(message)
    clientIP  = "Địa chỉ ip của client :{}".format(address)
    print(clientMsg)
    print(clientIP)
    s.sendto(str.encode("Hello client"), address)

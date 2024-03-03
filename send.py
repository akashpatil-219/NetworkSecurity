import socket

IP = '127.0.0.1' #local host - loopback addr
PORT = 9090
data = 'Hello, World!'

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP PACKET
sock.sendto(data.encode(),(IP,PORT))

#Test on different terminal window
# nc -luv 9090

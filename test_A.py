import socket
from SocketChannel import SocketChannel


message = "Hello world"
TCP_IP = '127.0.0.1'

channel = SocketChannel()
channel.connect(TCP_IP, 5005)

channel.send(message)
data = channel.receive()
print("received data from: ", data)
channel.close()
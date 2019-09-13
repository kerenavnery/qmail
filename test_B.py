import socket
from SocketChannel import SocketChannel


# message = str.encode("Hello world")

channel = SocketChannel(port=5005, listen=True)

data = channel.receive()
print("received data:", data.decode("utf-8"))
channel.close()
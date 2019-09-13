import socket
from SocketChannel import SocketChannel
import time


# message = str.encode("Hello world")

channel = SocketChannel(port=5005, listen=True)

data = channel.receive()
print("received data:", data.decode("utf-8"))
# time.sleep(1)
data = channel.receive()
print("received data:", data.decode("utf-8"))
channel.close()
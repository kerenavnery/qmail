import socket
from SocketChannel import SocketChannel
import Protocols as Prt






message = "Hello world"
TCP_IP = '127.0.0.1'

channel = SocketChannel()
channel.connect(TCP_IP, 5005)

channel.send(str.encode(message))
channel.close()

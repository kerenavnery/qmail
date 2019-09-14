from SocketChannel2 import SocketChannel

def main():
   channel = SocketChannel(1331, False)
   channel.connect('localhost', 1221)
   channel.send("Hello server")
   print("Recieved msg: %s".format{channel.recieve()})

if __name__ == "__main__":
    main()
from SocketChannel2 import SocketChannel
import Protocols
import pickle

ALICE_ADDR = 'localhost'
OSCAR_ADDR = 'localhost'
ALICE_PORT = 5005
OSCAR_PORT = 5006

def main():

  Protocols.oscar_sends('01', OSCAR_PORT, ALICE_PORT)

if __name__ == "__main__":
  main()
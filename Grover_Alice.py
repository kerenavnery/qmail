from SocketChannel2 import SocketChannel
import Protocols
import pickle

ALICE_ADDR = 'localhost'
OSCAR_ADDR = 'localhost'
ALICE_PORT = 5005
OSCAR_PORT = 5006

def main():
  # prepare message

  Protocols.multiparty_2grover_local( ALICE_PORT, OSCAR_PORT)

  pass

if __name__ == "__main__":
  main()
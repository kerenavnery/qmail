from SocketChannel2 import SocketChannel
import Protocols
import pickle

ALICE_ADDR = 'localhost'
BOB_ADDR = 'localhost'
ALICE_PORT = 5005
BOB_PORT = 5006

def main():

  Protocols.receive_a_qmail(BOB_PORT, ALICE_ADDR, ALICE_PORT)

  pass

if __name__ == "__main__":
  main()
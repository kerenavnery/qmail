from SocketChannel2 import SocketChannel
import Protocols
import pickle

ALICE_ADDR = 'localhost'
BOB_ADDR = 'localhost'
ALICE_PORT = 5005
BOB_PORT = 5006

def main():
  # prepare message
  message = "Hello Qiskit!"

  Protocols.send_a_qmail(message, ALICE_PORT, BOB_ADDR, BOB_PORT)

  pass

if __name__ == "__main__":
  main()
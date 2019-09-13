import socket

class QuantumChannel:
  """
  Faked quantum channel
  """
  def __init__(self, socket=None):


  def connect(self, host, port):
        self.sock.connect((host, port))

  def sendQbit(self, msg):
      # totalsent = 0
      # while totalsent < MSGLEN:
      #     sent = self.sock.send(msg[totalsent:])
      #     if sent == 0:
      #         raise RuntimeError("socket connection broken")
      #     totalsent = totalsent + sent

  def receiveQbit(self):
      # chunks = []
      # bytes_recd = 0
      # while bytes_recd < MSGLEN:
      #     chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
      #     if chunk == b'':
      #         raise RuntimeError("socket connection broken")
      #     chunks.append(chunk)
      #     bytes_recd = bytes_recd + len(chunk)
      # return b''.join(chunks)
import socket

class SocketChannel:
  """
  Class for a classical channel
  """

  def __init__(self, port=5005, listen=False):
    """
      If listen is true party acts as receiver
    """

    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.TCP_PORT = port
    self.BUFFER_SIZE = 2048
    self.MSGLEN = 2048
    if listen:
      self.sock.bind(('127.0.0.1', self.TCP_PORT))
      # self.sock.bind((socket.gethostname(), self.TCP_PORT))
      self.sock.listen(1)
      self.sock, addr = self.sock.accept()
      print('Connection address:', addr)

  def connect(self, host, port):
    self.sock.connect((host, port))
    
  def close(self):
    self.sock.close()

  def send(self, msg):
    self.sock.send(str.encode(msg))
    # totalsent = 0
    # while totalsent < self.MSGLEN:
    #   sent = self.sock.send(msg[totalsent:])
    #   if sent == 0:
    #     raise RuntimeError("socket connection broken")
    #   totalsent = totalsent + sent

  def receive(self):
    data = self.sock.recv(self.BUFFER_SIZE)
    # convert to string
    datastr = data.decode("utf-8") 
    return datastr

    # chunks = []
    # bytes_recd = 0
    # while bytes_recd < self.MSGLEN:
    #   chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, self.BUFFER_SIZE))
    #   if chunk == b'':
    #     raise RuntimeError("socket connection broken")
    #   chunks.append(chunk)
    #   bytes_recd = bytes_recd + len(chunk)
    #   print(str(bytes_recd))
    # return b''.join(chunks)
  
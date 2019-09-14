from collections import deque
import time
import random
import multiprocessing
import threading

MAX_LEN = 10
buff = deque(maxlen=MAX_LEN)

class Consumer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    while True:
      print("Consumer: hola")
      while len(buff) <= 0:
        print("Consumer: the buff is empty, waiting...", buff)
        time.sleep(1)
      buff.pop()


class Producer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  
  def run(self):
    while True:
      print("Producer: hola")
      while len(buff) >= MAX_LEN:
        print("Producer: buff is full, waiting...", buff)
        time.sleep(1)
      buff.append(random.randint(1,9))

if __name__ == '__main__':
  p = Producer()
  c = Consumer()

  p.start()
  c.start()
  p.join()
  c.join()


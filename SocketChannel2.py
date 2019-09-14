#!/usr/bin/env python

import asyncio
import websockets
import threading
from collections import deque
import time

class SocketChannel(threading.Thread):

	async def handler(self, websocket, path):
		with self.lock:
			#print(str(self.port) + "get lock")
			async for message in websocket:
				# TODO: Add to message to consumer queue
				self.producer(message)
				#print(message)
				# print("---")
			#print(str(self.port) + "release lock")

	def __init__(self, port=5005, listen=False):
		self.port = port
		threading.Thread.__init__(self)
		self.lock = threading.Lock()
		self.start()
		# consumer/producer buffer
		self.BUFF_MAX_LEN = 1000
		self.buff = deque(maxlen=self.BUFF_MAX_LEN)

	def run(self):
		with self.lock:
			print("Running on port = " + str(self.port))
			loop = asyncio.new_event_loop()
			self.loop = loop
			asyncio.set_event_loop(loop)
			#asyncio.get_event_loop().
			loop.run_until_complete(websockets.serve(self.handler, 'localhost', self.port))
		loop.run_forever()

	def connect(self, host, port):
		self.otherIP = host
		self.otherport = port
		
	def close(self):
		pass

	def kill(self):
		print(str(self.port) + " Trying to kill myself")
		while(1):
			if self.lock.locked():
				time.sleep(1)
				print(str(self.port) + " Channel still in use...")
			else:
				with self.lock:
					#print(str(self.port) + "get lock")
					print("Killing myself")
					self.loop.call_soon_threadsafe(self.loop.stop)
					break
	def send(self, msg):
		asyncio.get_event_loop().run_until_complete(self.ws_send('ws://' + self.otherIP + ':' + str(self.otherport), msg))

	def receive(self):
		# TODO: Get element from queue or block if there is no element ready
		msg = self.consumer()
		#print("Received: ", msg)
		return msg
		
	async def ws_send(self, uri, msg):
		with self.lock:
			#print(str(self.port) + "get lock (send)")
			#print("Is sending...")
			async with websockets.connect(uri) as websocket:
				await websocket.send(msg)
			#print("Stop sending...")
			#print(str(self.port) + "release lock (send)")

	def producer(self, msg):
		# print("Producer: hola")
		while len(self.buff) >= self.BUFF_MAX_LEN:
			# print("SocketChannel: buffer is full, waiting...")
			time.sleep(1)
		self.buff.append(msg)

	def consumer(self):
		# print("Consumer: hola")
		while len(self.buff) <= 0:
			# print("SocketChannel: the buff is empty, waiting...")
			time.sleep(1)
		msg = self.buff.pop()
		return msg

## EXAMPLE
# # Initialize
#alice = SocketChannel(1221, True)
#bob = SocketChannel(1222, False)

#alice.connect('localhost', 1222)
#bob.connect('localhost', 1221)

# Send
#alice.send("Hello Alice here")
#alice.send("Hello Alice here2")
#alice.send("Hello Alice here3")
#bob.send("Hello Bob here")


#alice.receive()
#bob.receive()
#bob.receive()
#bob.receive()
#bob.receive()

#alice.kill()
#bob.kill()



#time.sleep(1)

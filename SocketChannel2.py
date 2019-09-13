#!/usr/bin/env python

import asyncio
import websockets
import threading

class SocketChannel(threading.Thread):

	async def handler(self, websocket, path):
		async for message in websocket:
			# TODO: Add to message to consumer queue
			print(message)
			print("---")

	def __init__(self, port=5005, listen=False):
		self.port = port
		threading.Thread.__init__(self)
		self.start()

	def run(self):
		print("RUNNNN... port = " + str(self.port))
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		#asyncio.get_event_loop().
		loop.run_until_complete(websockets.serve(self.handler, 'localhost', self.port))
		loop.run_forever()

	def connect(self, host, port):
		self.otherIP = host
		self.otherport = port
		
	def close(self):
		pass

	def send(self, msg):
		asyncio.get_event_loop().run_until_complete(self.ws_send('ws://' + self.otherIP + ':' + str(self.otherport), msg))

	def receive(self):
		# TODO: Get element from queue or block if there is no element ready
		pass
		
	async def ws_send(self, uri, msg):
	    async with websockets.connect(uri) as websocket:
	    	await websocket.send(msg)


# Initialize
#alice = SocketChannel(1221, True)
#bob = SocketChannel(1222, False)
#print("hjkkhj")

#alice.connect('localhost', 1222)
#bob.connect('localhost', 1221)

# Send
#print("asdf")
#alice.send("Hello Alice here")
#bob.send("Hello Bob here")




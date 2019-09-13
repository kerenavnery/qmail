from qiskit import *

from channel_class import Channel

#Bob Part
circ_bob = QuantumCircuit(3)

bob_channel = Channel()
circ_bob, offset = bob_channel.receive(circ_bob)#,to_tpc)
circ_bob.draw()



# Add new gates to circ2
circ_bob.h(0+offset)
#circ_bob.cx(0+offset, 1+offset)
#psi2 = Statevector.from_instruction(circ_bob)

to_tpc = bob_channel.send(circ_bob,[1])
circ_bob.draw()



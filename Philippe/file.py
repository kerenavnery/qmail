from qiskit import *
from qiskit.quantum_info import Statevector

basis_gates = ['u1', 'u2', 'u3', 'cx']

circ = QuantumCircuit(2)
circ.h(0)
circ.cx(0, 1)
psi1 = Statevector.from_instruction(circ)

# Initialize circ-2 in state psi (using transpile to remove reset)
circ2 = QuantumCircuit(2)
circ2.initialize(psi1.data, [0, 1])
circ2 = transpile(circ2, basis_gates=basis_gates)

# Add new gates to circ2
circ2.h(0)
circ2.cx(1, 0)
psi2 = Statevector.from_instruction(circ2)

psi2    

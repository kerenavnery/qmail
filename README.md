# qmail (Quantum Email and beyond)
Qiskit Hackaton Quantum Mail Implementation (#38)

## Overview
This implementation allows to send mails over a simulated quantum channel. It is realized using IBM's Qiskit quantum computing software development framework. This allows us to later replace our simulated channel with a real quantum channel.

## Simulating a quantum channel
Alice and Bob have both some number of local qubits. Additionally they share a quantum channel (shared qubits). So Alice can perform operations and measurements on her local qubits and the quantum channel, and similarly for Bob.

## Applications based on the quantum channel
We implemented several use cases for quantum channels:
### Quantum state exchange
Sending an arbitrary quantum state over the channel.
### Quantum email (with QOTP)
Sending messages over the quantum channel, encrypted using the Quantum One-Time-Pad.
### Quantum teleportation
Teleporting of a single qubit between two parties.
### Multiparty Grovers algorithm
Bob holds a database and allows Alice to search elements. 

## Usability
The quantum channel framework is easy to use. Custom applications can be implemented in a short amount of time due to the many examples given in the sections above.

## Members

- Luca Dolfi, Switzerland
- Marc Wyss, Switzerland
- Keren Avnery, Israel
- Cica Gustiani, Indonesia
- Philippe Suchsland, Germany

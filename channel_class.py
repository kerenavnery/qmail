from qiskit import *
from qiskit.quantum_info import Statevector

#From Marc
import parser

#From Luca
import socket
from SocketChannel import SocketChannel



class Channel:    
    def __init__(self,slave_offset=0):
        self._state_vector = None
        self._arr_qubits = None
        self._basis_gates = ['u1', 'u2', 'u3', 'cx','x','y','H','z']
        self._master = True
        self._offset = 0
        self._slave_offset = slave_offset
        
        self._circuit = None
        
    def send(self,circuit,arr_qubits):
        self._state_vector = Statevector.from_instruction(circuit)  
        self._arr_qubits = arr_qubits
        self._circuit = circuit      
 
        #From Marc
        ser = parser.QSerializer()
        ser.add_element('channel_class', self)
        str_to_send = ser.encode()

        #print(str_to_send.type())

        #From Luca
        message = str_to_send
        TCP_IP = '127.0.0.1'

        channel = SocketChannel()
        channel.connect(TCP_IP, 5005)

        channel.send(message)
        channel.close()
        
        ## TODO: TCP THINGS
        return self
        
    def receive(self,circuit):#,recieve_channel):  ## TODO: remove recieve as an input
        #TODO: TCP things
        #recieve_channel = TCP_STUFF
        
        #From Luca
        print('Wait to receive')
        channel = SocketChannel(port=5005, listen=True)
        data = channel.receive()
        print("received stuff \o/")
        #print("received data:", data)
        channel.close()
        
        #From Marc
        ser2 = parser.QSerializer()
        ser2.decode(data)
        recieve_channel = ser2.get_element('channel_class')
        
        self._slave_offset = recieve_channel._slave_offset
        if(recieve_channel._master):
            self._master = False
            self._offset = self._slave_offset
        
        new_circuit = QuantumCircuit(len(recieve_channel._state_vector.dims()))
        new_circuit.initialize(recieve_channel._state_vector.data, range(len(recieve_channel._state_vector.dims())))
        new_circuit = transpile(new_circuit, basis_gates=self._basis_gates)
        return recieve_channel._circuit, self._offset

        return new_circuit, self._offset   




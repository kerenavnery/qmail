#!/usr/bin/env python3
from qiskit import *
from qiskit.quantum_info import Statevector
from textwrap import wrap
from random import randrange
from SocketChannel2 import SocketChannel
import pickle


# Quantum One-Time pad related methods

def str_to_lbin(message, bin_size=4):
    """
    String to 8 bit binary per character

    :message:str, the message
    """
    clist = [ord(x) for x in message]
    bins = ''.join([format(x,'08b') for x in clist])
    return wrap(bins,bin_size)


def bins_to_str(lbin):
    """
    Return a list of unicode characters into a message 

    :lbin:list(bin), a list of characters
    """
    sbin = ''.join(lbin) 
    lbin8 = wrap(sbin, 8)
    message = chr(int(lbin8[0],2))
    for c in lbin8[1:]:
        message+=chr(int(c,2))

    return message
 

def encode_cinfo_to_qstate(cinfo_bin):
    """
    Return the quantum state that encodes the binary  

    :cinfo_bin:str, string of binary contains the classical information

    return :QuantumCircuit:
    """
    nreg = len(cinfo_bin)
    qcirc = QuantumCircuit(nreg, nreg)
    for i,bit_i in enumerate(cinfo_bin[::-1]):
        if int(bit_i):
            qcirc.x(i)
    return qcirc


def generate_otp_key(key_length):
    """
    Generate key_length random key for one-time pad
    """
    x_key=bin(randrange(2**key_length))[2:] 
    z_key=bin(randrange(2**key_length))[2:] 

    return {'x': x_key, 'z': z_key}


def otp_enc_dec(qcirc, otpkey):
    """
    :qcirc:QuantumCircuit instance
    :key:dict={x:, z:}
    """
    r_x , r_z = otpkey['x'], otpkey['z']
    for i,k in enumerate(zip(r_x,r_z)):
        if k[0]:
            qcirc.x(i)
        if k[1]:
            qcirc.z(i)



def qotp(qcirc, otpkey, qChannel=None):
    """
    Quantum one-time pad

    :qmessage:qiksit.QuantumCircuit 
    :otpkey: dict{x:int y:int} 
    :qChannel: quantum channel
    """
    #Alice's part: encoding
    otp_enc_dec(qcirc, otpkey)

    #Alice send the qubits
    #TODO:Channel stuff
    # send over Qchannel

    #Bob receives qubits, and decrypt them
    otp_enc_dec(qcirc, otpkey)

    #Bob measure the states, single shot
    simulator = Aer.get_backend('qasm_simulator')
    nqubit = len(otpkey['x'])
    for i in range(nqubit):
        qcirc.measure(range(nqubit), range(nqubit))
        counts = execute(qcirc, backend=simulator, shots = 1).result()

    output = list(counts.get_counts().keys())[0] 
    return output



def send_a_qmail(message, port, destAddr, destPort, batch_size=4):
    """ Alice sends to Bob a quantum email

    :nqubit:int, the number of qubits
    :message:str, the secret message that wants to be sent 
    """
    nqubit = batch_size

    print('Alice wants to send %s'%message)
    # Initialize with Bob
    classicC = SocketChannel(port, False)
    # connect to Bob
    classicC.connect(destAddr, destPort)

    #send message per batch bits
    Lbins = str_to_lbin(message, batch_size)

    #generate key
    print('generating key...')
    otpkey = generate_otp_key(len(Lbins)*batch_size)
    print('X-encryption key %s'%otpkey['x'], 'Z-encryption key %s'%otpkey['z'])

    # send key to Bob
    classicC.send(pickle.dumps(otpkey))
    print("I am Alice I sent:", otpkey)
    # close the classic channel as we don't need it anymore
    classicC.close()

    key_per_batch = [{'x':x,'z':z} for x,z in zip(wrap(otpkey['x'],batch_size),wrap(otpkey['z'],batch_size))]

    # TODO: setup quantum channel

    bob_meas_results = [] # Bob
    for bin_batch,k in zip(Lbins, key_per_batch):  
        print('Performing QOTP for string', bin_batch)
        qcirc = encode_cinfo_to_qstate(bin_batch) # Alice
        bob_meas_results.append(qotp(qcirc, k)) # Bob
        print('Bob measures',bob_meas_results[-1]) # Bob
 
    print('Bobs message %s'%bins_to_str(bob_meas_results)) #Bob
    return bins_to_str(bob_meas_results)

def receive_a_qmail(port, srcAddr, srcPort, batch_size=4):
        # Initialize with Bob
    classicC = SocketChannel(port, True)
    # connect to Bob
    classicC.connect(srcAddr, srcPort)

    # receive otpkey from alice
    otpkey = classicC.receive()
    otpkey = pickle.loads(otpkey)
    print("I am Bob I received: ", otpkey)
    classicC.close()

    key_per_batch = [{'x':x,'z':z} for x,z in zip(wrap(otpkey['x'],batch_size),wrap(otpkey['z'],batch_size))]

    # TODO: setup quantum channel
    # TODO: receive qcirc with quantum channel
    qcirc = None
    # TODO: decrypt and measure
    bob_meas_results = []
    for k in key_per_batch:
        bob_meas_results.append(qotp(qcirc, k))
        print('Bob measures',bob_meas_results[-1])
    print('Bobs message %s'%bins_to_str(bob_meas_results))

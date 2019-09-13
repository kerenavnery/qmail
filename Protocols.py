#!/usr/bin/env python3
from qiskit import *
from qiskit.quantum_info import Statevector
from textwrap import wrap
from random import randrange


def str_to_lbin(message, bin_size=4):
    """
    String to 8 bit binary per character

    :message: add the message
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



def qotp(qcirc, otpkey):
    """
    Quantum one-time pad

    :qmessage:qiksit.QuantumCircuit 
    :key: dict{x:int y:int} 
    :nqubit:int, the number of qubits
    """
    #Alice's part: encoding
    otp_enc_dec(qcirc, otpkey)

    #Alice send the qubits
    #Channel stuff

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



def send_a_qmail(message, batch_size=4):
    """ Alice sends to Bob a quantum email

    :nqubit:int, the number of qubits
    :message:int,  
    """
    nqubit = batch_size

    print('Alice wants to send %s', message)

    #send message per batch bits
    Lbins = str_to_lbin(message, batch_size)

    #generate key
    print('generating key...')
    otpkey = generate_otp_key(len(Lbins)*batch_size)
    print(otpkey)

    key_per_batch = [{'x':x,'z':z} for x,z in zip(wrap(otpkey['x'],batch_size),wrap(otpkey['z'],batch_size))]

    bob_meas_results = []
    for bin_batch,k in zip(Lbins, key_per_batch):  
        print('OTP for string', bin_batch)
        qcirc = encode_cinfo_to_qstate(bin_batch) 
        bob_meas_results.append(qotp(qcirc, k))
 
    print('Bobs message %s'%bins_to_str(bob_meas_results))
    return bins_to_str(bob_meas_results)



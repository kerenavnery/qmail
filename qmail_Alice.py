from qiskit import *
from channel_class import Channel
import Protocols as Prt
import parser as prs



def send_a_qmail(message, batch_size=4):
    """
    Non-local implementation of sending a quantum mail

    :message:str, the message to sent 
    :batch_size:int, the size of batch message per session
    """
    Lbins = Prt.str_to_lbin(message, batch_size)

    # assume that it is a classical secure  channel
    cschannel = 
    otpkey = generate_otp_key(len(Lbins)*batch_size) 
    
    parser = prs.Qserializer()
    parser.add_element('key', otpkey)
    msg_key = parser.encode()

    cchannel.send(msg_key)
    
    # the sender performs one-time pad 
    # encode the 

    n_master, n_slave = batch_size, batch_size 
    offset_master, offset_slave = 0, n_master    

    qcirc = QuantumCircuit(n_master + n_slave)
    channel = Channel(offset_slave)

    

    ## Master
    circ.h(0 + channel._offset)
    #circ.cx(0 + channel._offset, 1  + channel._offset)
    #irc.h(1 + channel._offset)


    to_tpc = channel.send(circ,[1])  ## TODO: remove
    circ.draw()


    #Alice Part
    circ_alice = QuantumCircuit(3)

    alice_channel = Channel()
    circ_alice , offset = alice_channel.receive(circ_alice)#,to_tpc)
    circ_alice.draw()




from qiskit import *
from channel_class import Channel



def receive_qmail():
    """
    Receive 
    """
    cchannel = Channel()
    otpkey = cchannel.receive()
    
    

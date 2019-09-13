import pickle

class QSerializer:
    def __init__(self):
        self.elements = {}

    # Add an element to the serializer (e.g: name = "statevector", obj = <the statevector object>)
    def add_element(self, name, obj):
        self.elements[name] = obj

    # Convert all the elements to one string
    def encode(self):
        return pickle.dumps(self.elements)

    # Input an encoded string
    def decode(self, encoded_string):
        self.elements = pickle.loads(encoded_string) 

    # Return the object of an element with a given name
    def get_element(self, name):
        return self.elements[name]

    # 
    def get_element_names(self):
        return self.elements.keys()
    
    # Delete all elements
    def clear(self):
        self.elements.clear()
        
# --- SAMPLE CODE ---
# import parser
# 
# ALICE:
# ser = parser.QSerializer()
# ser.add_element('statevector', statevector)
# str = ser.encode()

# BOB
# ser2 = parser.QSerializer()
# ser2.decode(str)
# mystatevector = ser2.get_element('statevector')

# assert statevector == mystatevector
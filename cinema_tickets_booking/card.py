

class Card():
    
    database_path = ""
    
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price):
        pass
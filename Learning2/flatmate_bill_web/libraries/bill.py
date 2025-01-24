class Bill:
    """
    Object contains data about a bill such total amount and period of bill
    """    
    def __init__(self, amount: float = 0, period: str = ""):
        
        self.amount = amount
        self.period = period
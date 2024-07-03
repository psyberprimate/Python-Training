class Flatmate:
    """
    Creates a flatmate object per person for paying share of the living costs in bill
    """    
    
    def __init__(self, name : str = "", days_in_house: int = 0):
        
        self.days_in = days_in_house
        self.name = name
        
        
    def pays(self, bill, other_flat_mate_days) -> float:
        weight = self.days_in / (self.days_in + other_flat_mate_days.days_in)
        return  weight * bill.amount
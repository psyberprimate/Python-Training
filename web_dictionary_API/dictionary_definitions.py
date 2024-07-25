import pandas as pd

class Definition:
    """Small class for making searches with pandas data
    frames from a dictionary on csv file
    """    
    def __init__(self, term : str):
        self.term = term
        
    def get(self) -> tuple:
        df = pd.read_csv("web_dictionary/data.csv")
        return tuple(df.loc[df['word']==self.term]['definition'])  
    
    
if __name__ == "__main__":
    d = Definition(term="Earth")
    print(d.get())
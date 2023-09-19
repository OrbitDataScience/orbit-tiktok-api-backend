import pandas as pd

def getTest(a, b):
    
    data  = {"col1": [a], "col2":[b]}
    df = pd.DataFrame(data=data)
    
    return df
from os import path
from typing import List
import pandas as pd

#extract from csv file
def readCSV(pathname:str)->List[List[str]]:
    df = pd.read_csv(pathname)
    return df.values.tolist()

#extract from excel file.
def readExcel(pathname:str)->List[List[str]]:
    df = pd.read_excel(pathname)
    return df.values.tolist() #idk if i should turn it back into a list, but for now wtv.

#check if path is correct and pass it to the appropriate function
def checkFile(pathname:str)->List[List[str]]:
    if path.isfile(pathname):
        file_extension = path.splitext(pathname)[1]
        if file_extension=='.csv':
            return 
        elif file_extension=='.xlsx':
            return readExcel(pathname)
        else:
            return None
    else:
        return None
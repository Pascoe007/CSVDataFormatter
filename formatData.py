import pandas as pd

class FormatData:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_csv(self.file)
        self.data.columns = [c.replace(' ', '_') for c in self.data.columns]
        self.data.columns = [c[c.find(':')+1 :  : ] if c.find(':') else c for c in self.data.columns]
        #self.data.columns = [c.replace(':', '') for c in self.data.columns]
    
    def SaveData(self, path):
        self.data.to_csv(path, index = False)
    
    def FormatRows(self, colunmName, values):
        column = self.data[colunmName].tolist()
        for item in range(len(column)):
            if column[item] not in (values):
                self.data.drop(item, inplace= True)
        self.data = self.data.reset_index(drop=True)

    def GetHeaders(self):
        return list(self.data)

    def GetUniqueValues(self, columnName):
        return self.data[columnName].unique()
    
    
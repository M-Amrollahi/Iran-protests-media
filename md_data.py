import pandas as pd

path_dataset = "./data/dataset.csv"

class cls_data(object):
    
    def __init__(self):
        self.df = pd.read_csv(path_dataset)
        if "status" not in self.df.columns:
            self.df["status"] = 0
        print(self.df.status.value_counts())
        
    def f_getDF(self):
        return self.df

    def f_saveDF(self):
        print(self.df.status.value_counts())
        self.df.to_csv(path_dataset, index=False)
    
    def f_updateStatus(self,dict_sr):
        for i in dict_sr.keys():
            self.df.loc[i,"status"] = 1

    def f_getNotDLIndeces(self):
        return self.df.loc[self.df.status == 0].index.to_list()

import pandas as pd
class Univariate():
    
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        
        for columnName in dataset.columns:
            # print (columnName)
            if dataset[columnName].dtypes=='O':
                # print("Qual")
                Qual.append(columnName)
            else:
                # print("Quan")
                Quan.append(columnName)
        return Quan, Qual

    def uni_variate(dataset,Quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%","100%","IQR",
                                   "1.5IQR","LesserRange","GreaterRange", "Min Value", "Max Value","Kurtosis","Skewness","Variance","STD"],columns=Quan)
        for columnName in Quan:
            descriptive[columnName]["Mean"] = dataset[columnName].mean()
            descriptive[columnName]["Median"] = dataset[columnName].median()
            descriptive[columnName]["Mode"] = dataset[columnName].mode()[0]
        
            descriptive[columnName]["25%"] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]["50%"] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]["75%"] = dataset.describe()[columnName]["75%"]
            descriptive[columnName]["100%"] = dataset.describe()[columnName]["max"]
        
            descriptive[columnName]["IQR"] = descriptive[columnName]["75%"] - descriptive[columnName]["25%"]
        
            descriptive[columnName]["1.5IQR"] = 1.5 * descriptive[columnName]["IQR"]
        
            descriptive[columnName]["LesserRange"] = descriptive[columnName]["25%"] - descriptive[columnName]["1.5IQR"]
        
            descriptive[columnName]["GreaterRange"] = descriptive[columnName]["75%"] + descriptive[columnName]["1.5IQR"]
        
            descriptive[columnName]["Min Value"] = dataset[columnName].min()
            descriptive[columnName]["Max Value"] = dataset[columnName].max()
            descriptive[columnName]["Kurtosis"] = dataset[columnName].kurtosis()
            descriptive[columnName]["Skewness"] = dataset[columnName].skew()
            descriptive[columnName]["Variance"] = dataset[columnName].var()
            descriptive[columnName]["STD"] = dataset[columnName].std()
        return descriptive

    def CheckOutliers(descriptive,Quan):
        lesser=[]
        greater=[]
        for columnName in Quan:
            if(descriptive[columnName]["Min Value"]<descriptive[columnName]["LesserRange"]):
                lesser.append(columnName)
            if(descriptive[columnName]["Max Value"]>descriptive[columnName]["GreaterRange"]):
                greater.append(columnName)
        return lesser,greater

    def ReplacingOutlier(lesser, greater,descriptive,dataset):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["LesserRange"]]=descriptive[columnName]["LesserRange"]
        for columnName in greater:
             dataset[columnName][dataset[columnName]>descriptive[columnName]["GreaterRange"]]=descriptive[columnName]["GreaterRange"]
    
    def FreqTable(dataset,columnName):
            freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","CumSum"])
            freqTable["Unique_Values"]=dataset[columnName].value_counts().index  # ".index" to take only the index va;ues
            freqTable["Frequency"]=dataset[columnName].value_counts().values
            freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
            freqTable["CumSum"]=freqTable["Relative_Frequency"].cumsum() 
            return freqTable
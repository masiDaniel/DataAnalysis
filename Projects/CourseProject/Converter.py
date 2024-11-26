import pandas as pd 

#read the raw data from the text file 
df = pd.read_csv('titanic_data.txt')

#save it to an excel file
df.to_csv("titanic.csv", index= False)

print("Data sucesfully converted and saved")

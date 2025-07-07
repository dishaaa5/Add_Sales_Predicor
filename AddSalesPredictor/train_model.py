import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

#load the dataset
df = pd.read_csv(r"C:\Users\Dell\OneDrive\New folder\AIML(all basics)\AddSalesapp.py\6 advertising.csv")

#prepare features and target
X = df[["TV" , "Radio" , "Newspaper"]]
Y = df["Sales"]


#train model
model = LinearRegression()
model.fit(X,Y)


#save the trained model as a pickle file
with open("ad_sales_model.pkl" , "wb") as f:
    pickle.dump(model,f)

print("Model trained and saved as ad_sales_model.pkl")    



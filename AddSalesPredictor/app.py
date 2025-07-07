import streamlit as st
import pickle
import pandas as pd

with open(r"C:\Users\Dell\OneDrive\New folder\AIML(all basics)\AddSalesapp.py\ad_sales_model.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("Ad Sales Prediction App")
st.write("Enter advertising budgets below to predict product sales:")

# Input fields
tv = st.number_input("TV Budget ($)", min_value=0.0, max_value=300.0, value=150.0)
radio = st.number_input("Radio Budget ($)", min_value=0.0, max_value=100.0, value=25.0)
newspaper = st.number_input("Newspaper Budget ($)", min_value=0.0, max_value=100.0, value=20.0)

# Prediction on button click
if st.button("Predict Sales"):
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "Radio", "Newspaper"])
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Sales: **{prediction:.2f} units**")

st.caption("Made with using Pickle and Streamlit")

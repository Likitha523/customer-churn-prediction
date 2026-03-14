import streamlit as st
import numpy as np
import joblib
pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details:")

tenure = st.number_input("Tenure")
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):

    data = np.array([[tenure, monthly, total]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer will stay")

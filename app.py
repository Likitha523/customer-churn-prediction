import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("customer_churn_model.keras")

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender",[0,1])
senior = st.selectbox("Senior Citizen",[0,1])
partner = st.selectbox("Partner",[0,1])
dependents = st.selectbox("Dependents",[0,1])
tenure = st.number_input("Tenure",0,100)
phoneservice = st.selectbox("Phone Service",[0,1])
multiple = st.selectbox("Multiple Lines",[0,1])
internet = st.selectbox("Internet Service",[0,1,2])
security = st.selectbox("Online Security",[0,1])
backup = st.selectbox("Online Backup",[0,1])
device = st.selectbox("Device Protection",[0,1])
tech = st.selectbox("Tech Support",[0,1])
tv = st.selectbox("Streaming TV",[0,1])
movies = st.selectbox("Streaming Movies",[0,1])
contract = st.selectbox("Contract",[0,1,2])
paperless = st.selectbox("Paperless Billing",[0,1])
payment = st.selectbox("Payment Method",[0,1,2,3])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):

    input_data = np.array([[gender, senior, partner, dependents, tenure,
                            phoneservice, multiple, internet, security,
                            backup, device, tech, tv, movies,
                            contract, paperless, payment,
                            monthly, total]])

    prediction = model.predict(input_data)

    if prediction > 0.5:
        st.error("Customer will CHURN")
    else:
        st.success("Customer will stay")

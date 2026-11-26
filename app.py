import streamlit as st 
import pandas as pd
import numpy as np 

st.title("AI Poultry Farming Prediction System")

st.write(
    "Welcome! This application helps poultry farmers"
    "estimate broiler bird weight."
)

st.header("Enter Your Poultry Information")

age = st.number_input(
    "Bird Age (in weeks)",
    min_value=1,
    max_value=10,
    value=4
)

feed = st.number_input(
    "Daily Feed Consumption (grams per bird)",
    min_value=0,
    value=100
)

weight = st.number_input(
    "Current Average Bird Weight (grams)",
    min_value=0,
    value=500
)

if st.button("Analyze Poultry Data"):
    
    st.success("Your poultry information has been recorded!")
    
    st.write("Bird Age:", age, "weeks")
    st.write("Daily Feed:", feed, "grams")
    st.write("Current Weight:", weight, "grams")
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Diabetes Prediction Clinic", layout="centered")

# Main Title and Description
st.title("🏥 Patient Diabetes Risk Prediction")
st.markdown("""
This application is designed for healthcare providers to predict the likelihood of diabetes 
based on patient health attributes using a **Gradient Boosting Classifier**.
""")

# Sidebar for Patient Data Input
st.sidebar.header("Input Patient Metrics")

# Creating input fields for the features described in your problem statement
preg = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=0)
plas = st.sidebar.number_input("Plasma Glucose Concentration", min_value=0, max_value=300, value=100)
pres = st.sidebar.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
skin = st.sidebar.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
test = st.sidebar.number_input("Serum Insulin (mu U/ml)", min_value=0, max_value=900, value=80)
mass = st.sidebar.number_input("BMI (Weight in kg/m²)", min_value=0.0, max_value=70.0, value=25.0)
pedi = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.sidebar.number_input("Age (Years)", min_value=0, max_value=120, value=30)

# Displaying the input data for verification
st.subheader("Current Patient Profile")
input_data = {
    'Pregnancies': preg,
    'Glucose': plas,
    'Blood Pressure': pres,
    'Skin Thickness': skin,
    'Insulin': test,
    'BMI': mass,
    'Pedigree': pedi,
    'Age': age
}
st.table(pd.DataFrame([input_data]))

# Prediction Button
if st.button("Run Diabetes Assessment"):
    st.info("The MLOps pipeline is functioning correctly. Next step: Load the trained Gradient Boosting model.")

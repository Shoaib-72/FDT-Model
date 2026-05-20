import streamlit as st
import joblib
import pandas as pd

model=joblib.load("fdt_model.pkl")

st.set_page_config(page_title="FDT Optimization App",layout="centered")

st.title("💊 FDT Disintegration Time Predictor")
st.write("Predict and optimize Fast Dissolving Tablet formulation using ML")

st.divider()

# Input Section
st.subheader("Enter Formulation Parameters")

superdis = st.selectbox(
    "Superdisintegrant Type",
    ["CCS", "SSG", "CP"]
)

concentration = st.slider(
    "Concentration (%)",
    min_value=2,
    max_value=5,
    value=3
)

binder = st.slider(
    "Binder (%)",
    min_value=2,
    max_value=5,
 
    value=3
)

compression = st.slider(
    "Compression Force (kN)",
    min_value=4,
    max_value=7,
    value=5
)

st.divider()

# Prediction
if st.button("Predict Disintegration Time"):
    
    input_data = pd.DataFrame([[
        superdis,
        concentration,
        binder,
        compression
    ]],
    columns=[
        "Superdisintegrant",
        "Concentration (%)",
        "Binder (%)",
        "Compression (kN)"
    ])
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Disintegration Time: {round(prediction,2)} seconds")

st.divider()
st.caption("AI-based Optimization of Fast Dissolving Tablets")
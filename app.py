import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

@st.cache_resource
def load_model():
    df = pd.read_csv("Dataset/fdt_dataset_100_rows.csv")
    
    X = df.drop(columns=["Formulation", "Disintegration Time (sec)"])
    y = df["Disintegration Time (sec)"]
    
    preprocessor = ColumnTransformer(transformers=[
        ("cat", OneHotEncoder(drop="first"), ["Superdisintegrant"]),
        ("num", "passthrough", ["Concentration (%)", "Binder (%)", "Compression (kN)"])
    ])
    
    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("regressor", LinearRegression())
    ])
    model.fit(X, y)
    return model

model = load_model()

st.set_page_config(page_title="FDT Optimization App", layout="centered")
st.title("💊 FDT Disintegration Time Predictor")
st.write("Predict and optimize Fast Dissolving Tablet formulation using ML")
st.divider()

st.subheader("Enter Formulation Parameters")

superdis = st.selectbox("Superdisintegrant Type", ["CCS", "SSG", "CP"])
concentration = st.slider("Concentration (%)", min_value=2, max_value=5, value=3)
binder = st.slider("Binder (%)", min_value=2, max_value=5, value=3)
compression = st.slider("Compression Force (kN)", min_value=4, max_value=7, value=5)

st.divider()

if st.button("Predict Disintegration Time"):
    input_data = pd.DataFrame([[superdis, concentration, binder, compression]],
        columns=["Superdisintegrant", "Concentration (%)", "Binder (%)", "Compression (kN)"])
    
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Disintegration Time: {round(prediction, 2)} seconds")

st.divider()
st.caption("AI-based Optimization of Fast Dissolving Tablets")

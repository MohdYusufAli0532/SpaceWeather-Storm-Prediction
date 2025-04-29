import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('xgb_storm_classifier.pkl')

st.set_page_config(page_title="Space Weather Storm Predictor", layout="centered")
st.title("🔭 Space Weather Storm Predictor")
st.markdown("Predict whether a geomagnetic storm will occur based on space weather features.")

# Input features
st.sidebar.header("Input Features")

def user_input():
    kp = [st.sidebar.slider(f'Kp{i}', 0.0, 9.0, 2.0) for i in range(1, 9)]
    AE = st.sidebar.slider("AE Index", 0.0, 2000.0, 300.0)
    AL = st.sidebar.slider("AL Index", -2500.0, 0.0, -300.0)
    AU = st.sidebar.slider("AU Index", 0.0, 1500.0, 200.0)
    Ap = st.sidebar.slider("Ap Index", 0.0, 400.0, 15.0)
    F107 = st.sidebar.slider("F10.7 Solar Flux", 60.0, 300.0, 100.0)

    features = kp + [AE, AL, AU, Ap, F107]
    return np.array(features).reshape(1, -1)

input_data = user_input()

if st.button("Predict Storm"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Likely Storm (Confidence: {proba:.2f})")
    else:
        st.success(f"✅ No Storm Expected (Confidence: {1 - proba:.2f})")

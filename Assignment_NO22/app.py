import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Assignment_NO22/heart_model.pkl")
columns = joblib.load("Assignment_NO22/columns.pkl")

st.title("Heart Disease Prediction")

age = st.number_input("Age", 1, 120, 45)
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
bp = st.number_input("Resting Blood Pressure", 80, 250, 120)
chol = st.number_input("Cholesterol", 0, 700, 200)
fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
maxhr = st.number_input("Maximum Heart Rate", 60, 220, 150)
angina = st.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    sample = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "ChestPainType": cp,
        "RestingBP": bp,
        "Cholesterol": chol,
        "FastingBS": fbs,
        "RestingECG": ecg,
        "MaxHR": maxhr,
        "ExerciseAngina": angina,
        "Oldpeak": oldpeak,
        "ST_Slope": slope
    }])

    sample = pd.get_dummies(sample)
    sample = sample.reindex(columns=columns, fill_value=0)

    prediction = model.predict(sample)[0]

    if prediction == 1:
        st.error("Heart Disease: Yes")
    else:
        st.success("Heart Disease: No")
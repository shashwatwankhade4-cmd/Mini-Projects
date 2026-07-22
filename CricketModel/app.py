# ==========================
# Q1. Import Libraries
# ==========================

# Streamlit is used to create the web application.
import streamlit as st

# Pandas is used to create and manipulate DataFrames.
import pandas as pd

# Joblib is used to load the saved model and preprocessing files.
import joblib

# ==========================
# Q2. Load Model & Objects
# ==========================

model = joblib.load("CricketModel/LR_ODI.pkl")
scaler = joblib.load("CricketModel/scaler.pkl")
encoded_columns = joblib.load("CricketModel/columns.pkl")

# ==========================
# Q3. Page Configuration
# ==========================

# Configure the Streamlit page.
st.set_page_config(
    page_title="ODI Runs Predictor",
    layout="centered"
)

# ==========================
# Q4. Title & Description
# ==========================

st.title("🏏 ODI Runs Prediction")

st.write("Enter the batsman's details below to predict the expected ODI runs.")

# ==========================
# Q5 & Q6 Input Fields
# ==========================

# Numerical Inputs
mat = st.number_input("Matches", min_value=1, max_value=600, value=50)
inns = st.number_input("Innings", min_value=1, max_value=600, value=45)
no = st.number_input("Not Outs", min_value=0, max_value=200, value=5)
hs = st.number_input("Highest Score", min_value=0, max_value=300, value=100)
avg = st.number_input("Batting Average", min_value=0.0, value=40.0)
bf = st.number_input("Balls Faced", min_value=0, value=3000)
sr = st.number_input("Strike Rate", min_value=0.0, value=90.0)
hundreds = st.number_input("100s", min_value=0, value=5)
fifties = st.number_input("50s", min_value=0, value=20)
ducks = st.number_input(
    "Ducks (0)",
    min_value=0,
    value=0
)
# Text Input
player = st.text_input("Player Name")

# ==========================
# Q7 Predict Button
# ==========================

if st.button("Predict Runs"):

    # Create input dataframe
    data = pd.DataFrame({
        "Player": [player],
        "Mat": [mat],
        "Inns": [inns],
        "NO": [no],
        "HS": [hs],
        "Ave": [avg],
        "BF": [bf],
        "SR": [sr],
        "100": [hundreds],
        "50": [fifties],
        "0": [ducks]
    })

    # One-Hot Encoding
    data = pd.get_dummies(data)

    # Match training columns
    data = data.reindex(columns=encoded_columns, fill_value=0)

    # Scale numeric columns
    scale_cols = [
        "Mat",
        "Inns",
        "NO",
        "HS",
        "Ave",
        "BF",
        "SR",
        "100",
        "50",
        "0"
    ]

    data[scale_cols] = scaler.transform(data[scale_cols])

    # Prediction
    prediction = model.predict(data)

    # Display result
    st.success(f"Predicted Runs: {prediction[0]:.2f}")
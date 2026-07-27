

import streamlit as st

# Pandas is used for creating and manipulating DataFrames.
import pandas as pd

# Joblib is used for loading the trained model and preprocessing objects.
import joblib


model = joblib.load("Model/LR_ford_car.pkl")
scaler = joblib.load("Model/scaler.pkl")
encoded_columns = joblib.load("Model/columns.pkl")



st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)

st.title("🚗 Ford Car Price Predictor")

st.write(
    "Enter the car specifications below to predict its selling price."
)

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2025,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=300000,
    value=30000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    max_value=600,
    value=150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    max_value=150.0,
    value=55.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.8,
    max_value=6.0,
    value=1.5
)

# Selectbox prevents invalid inputs and
# provides a user-friendly dropdown.

transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual", "Semi-Auto"]
)

fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

model_name = st.text_input(
    "Car Model",
    value="Fiesta"
)

predict = st.button("Predict Price")

if predict:

    try:

        input_df = pd.DataFrame({

            "model": [model_name],
            "year": [year],
            "transmission": [transmission],
            "mileage": [mileage],
            "fuelType": [fuelType],
            "tax": [tax],
            "mpg": [mpg],
            "engineSize": [engineSize]

        })

        # One-Hot Encoding
        input_df = pd.get_dummies(input_df)

        # Align columns with training data
        input_df = input_df.reindex(
            columns=encoded_columns,
            fill_value=0
        )

        # Numerical columns
        numeric_cols = [
            "year",
            "mileage",
            "tax",
            "mpg",
            "engineSize"
        ]

        # Scale numerical columns
        input_df[numeric_cols] = scaler.transform(
            input_df[numeric_cols]
        )

        # Prediction
        prediction = model.predict(input_df)[0]

        st.success(
            f"Predicted Selling Price: £{prediction:,.2f}"
        )

    except Exception as e:
        st.error(f"Error: {e}")
        






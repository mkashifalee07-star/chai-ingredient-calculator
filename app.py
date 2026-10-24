
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Chai Ingredient Calculator", page_icon="☕")

st.title("☕ Chai Ingredient Calculator")
st.write("Enter the number of cups to calculate chai ingredients.")

try:
    if not os.path.exists("chai_model.pkl"):
        st.error("chai_model.pkl file nahi mili. GitHub par file check karo.")
    else:
        model = joblib.load("chai_model.pkl")

        cups = st.number_input(
            "Number of cups",
            min_value=1,
            max_value=100,
            value=4,
            step=1
        )

        if st.button("Calculate Ingredients"):
            input_data = pd.DataFrame({"cups": [cups]})
            prediction = model.predict(input_data)

            st.write("Model output:", prediction)
            st.write("Prediction shape:", prediction.shape)

except Exception as e:
    st.error(f"Error: {e}")

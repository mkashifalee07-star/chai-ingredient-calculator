
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Chai Ingredient Calculator", page_icon="☕")

st.title("☕ Chai Ingredient Calculator")
st.write("Enter the number of cups to calculate chai ingredients.")

@st.cache_resource
def load_model():
    return joblib.load("chai_model.pkl")

try:
    if not os.path.exists("chai_model.pkl"):
        st.error("chai_model.pkl file nahi mili. Check karo ke file app.py ke saath GitHub par hai.")
    else:
        model = load_model()

        cups = st.number_input(
            "Number of cups",
            min_value=1,
            max_value=100,
            value=4,
            step=1
        )

        if st.button("Calculate Ingredients"):
            input_data = pd.DataFrame({"cups": [cups]})
            prediction = model.predict(input_data)[0]
            st.write("Model prediction:", prediction)

            st.subheader(f"Ingredients for {cups} cups")
            st.write(f"🥛 Milk: {prediction[0]:.1f} ml")
            st.write(f"💧 Water: {prediction[1]:.1f} ml")
            st.write(f"🍃 Tea: {prediction[2]:.1f} g")
            st.write(f"🍬 Sugar: {prediction[3]:.1f} g")

except Exception as e:
    st.error(f"Model load ya prediction error: {e}")

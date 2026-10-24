
import streamlit as st
import pandas as pd
import joblib
import os
import traceback

st.set_page_config(page_title="Chai Ingredient Calculator", page_icon="☕")
st.title("☕ Chai Ingredient Calculator")
st.write("Enter the number of cups to calculate chai ingredients.")

if not os.path.exists("chai_model.pkl"):
    st.error("chai_model.pkl file nahi mili.")
else:
    try:
        model = joblib.load("chai_model.pkl")
        st.success("Model successfully loaded!")

        cups = st.number_input("Number of cups", 1, 100, 4)

        if st.button("Calculate Ingredients"):
            try:
                input_data = pd.DataFrame({"cups": [cups]})
                prediction = model.predict(input_data)

                st.write("Prediction output:", prediction)
                st.write("Prediction type:", type(prediction).__name__)
                st.write("Prediction shape:", getattr(prediction, "shape", "No shape"))

            except Exception:
                st.error("Prediction ke waqt error aya:")
                st.code(traceback.format_exc())

    except Exception:
        st.error("Model load karte waqt error aya:")
        st.code(traceback.format_exc())

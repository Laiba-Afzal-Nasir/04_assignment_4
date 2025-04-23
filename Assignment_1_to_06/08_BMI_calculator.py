# BMI Calculator

import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮",layout="centered")
st.title("🧮 BMI Calculator")
st.write("**Enter your height (in meters) and weight (in kg) to calculate your BMI**")

weight = st.number_input("Weight (in kilograms):", min_value=1.0, max_value=300.0, value=70.0, format="%.2f")
height = st.number_input("Height (in meters):", min_value=0.5, max_value=2.5, value=1.75, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.error("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.info("You are obese.")
    else:
        st.warning("Please enter a valid height and weight.")
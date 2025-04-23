# Buil a python website in 15 minutes with streamlit

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", page_icon="📊",layout="centered")
st.title("🎓 Student Data Generator")

names = ["Daniyal","Hammad","Reebal","Taha","Asad","Moiz","Jibran","Rohan","Zaviyar","Asmar","Arhum","Nabeel","Buhan","Rizwan","Noman","Roman","Hamdan"]

students = []

for i in range(1,18):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18,25),
        "Grade": random.choice(["A","B","C","D","E","F"]),
        "Marks": random.randint(40,100)
    }

    students.append(student)

data = pd.DataFrame(students)
st.subheader("📊 Student Data")
st.dataframe(data)

st.subheader("📊 Marks Bar Chart")
st.bar_chart(data['Marks'])

csv_file = data.to_csv(index=False).encode("utf-8")
if st.download_button("⬇️ Download CSV File",csv_file, "students.csv","text/csv"):
    st.success("✅ Students Data Generated Sucesssfully!")
import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

st.set_page_config(layout='wide')

st.title("Students' GPA Prediction App")

st.caption("This app helps to predict a students' GPA")

st.divider()

age = st.number_input("Enter the age of student", min_value=13, max_value=25, value=13, step=1)
gender = st.selectbox("What is the student's gender? ", ["Male", "Female"])
ethnicity = st.selectbox("What is the student's ethnicity? ", ["Caucasian", "African American", "Asian", "Other"])
parentalEducation = st.selectbox("What is their parent's education level ? ", ["None", "High School", "Some College", "Bachelor's", "Higher"])
studyTimeWeekly = st.number_input("How much time does the student spend studying weekly? ", min_value=0, max_value=500, value=0, step=1)
absences = st.number_input("How many times has the student been absent? ", min_value=0, max_value=50, value=0, step=1)
tutoring = st.selectbox("Does the student have a tutor? ", ["Yes", "No" ])
parentalSupport = st.selectbox("How involved are the students' parents? ", ["None", "Low", "Moderate", "High", "Very High"])
extracurricular = st.selectbox("Does the student participate in extracurricular activities? ", ["Yes", "No" ])
sports = st.selectbox("Does the student play sports?", ["Yes", "No"])
music = st.selectbox("Does the student partake in music activities?", ["Yes", "No"])
volunteering = st.selectbox("Does the student volunteer?", ["Yes", "No"])

predictbutton = st.button("Predict GPA")

st.divider()

model = joblib.load("nnmodel.pkl")


if gender == "Female":
    gender_pred = 1
else:
    gender_pred = 0
    

if ethnicity == "Caucasian":
    ethnicity_pred = 0
elif ethnicity == "African American":
    ethnicity_pred = 1
elif ethnicity == "Asian":
    ethnicity_pred = 2
else:
    ethnicity_pred = 3


if parentalEducation == "None":
    parentalEducation_pred = 0
elif parentalEducation == "High School":
    parentalEducation_pred = 1
elif parentalEducation == "Some College":
    parentalEducation_pred = 2
elif parentalEducation == "Bachelor's":
    parentalEducation_pred = 3
else:
    parentalEducation_pred = 4


if tutoring == "Yes":
    tutoring_pred = 1
else:
    tutoring_pred = 0


if parentalSupport == "None":
    parentalSupport_pred = 0
elif parentalSupport == "Low":
    parentalSupport_pred = 1
elif parentalSupport == "Moderate":
    parentalSupport_pred = 2
elif parentalSupport == "High":
    parentalSupport_pred = 3
else:
    parentalSupport_pred = 4


if extracurricular == "Yes":
    extracurricular_pred = 1
else:
    extracurricular_pred = 0


if sports == "Yes":
    sports_pred = 1
else:
    sports_pred = 0


if music == "Yes":
    music_pred = 1
else:
    music_pred = 0


if volunteering == "Yes":
    volunteering_pred = 1
else:
    volunteering_pred = 0

if predictbutton:
    st.snow()

    prediction = model.predict([[age, gender_pred, ethnicity_pred, parentalEducation_pred, studyTimeWeekly, absences, tutoring_pred, parentalSupport_pred, extracurricular_pred, sports_pred, music_pred, volunteering_pred]])

    st.write(prediction)


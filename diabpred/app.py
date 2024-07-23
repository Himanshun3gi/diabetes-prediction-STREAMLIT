import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Diabetes Prediction")

# User inputs
st.sidebar.header("Patient Data")
def user_input_features():
    gender = st.sidebar.selectbox("Gender", ["Female", "Male"])  # Collecting for informational purposes
    age = st.sidebar.slider("Age", 0, 120, 25)
    hypertension = st.sidebar.selectbox("Hypertension", [0, 1])
    heart_disease = st.sidebar.selectbox("Heart Disease", [0, 1])
    smoking_history = st.sidebar.selectbox("Smoking History", ["Never", "Former", "Current"])  # Collecting for informational purposes
    bmi = st.sidebar.slider("BMI", 0.0, 70.0, 25.0)
    HbA1c_level = st.sidebar.slider("HbA1c Level", 0.0, 20.0, 5.0)
    blood_glucose_level = st.sidebar.slider("Blood Glucose Level", 0, 500, 100)
    
    data = {
        'age': age,
        'hypertension': hypertension,
        
        'bmi': bmi,
        'HbA1c_level': HbA1c_level,
        'blood_glucose_level': blood_glucose_level
    }
    features = pd.DataFrame(data, index=[0])
    return features, gender, smoking_history

df, gender, smoking_history = user_input_features()

# Display user input
st.subheader("User Input")
st.write("Gender: ", gender)
st.write("Smoking History: ", smoking_history)
st.write(df)

# Prediction
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader("Prediction")
st.write("Diabetes" if prediction[0] == 1 else "No Diabetes")

st.subheader("Prediction Probability")
st.write(prediction_proba)

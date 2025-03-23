import streamlit as st
import pandas as pd
import joblib


parkinson_model = joblib.load("models/parkinson_model.pkl")
diabetes_model = joblib.load("models/diabetes_model.pkl")
heart_disease_model = joblib.load("models/heart_disease_model.pkl")
lung_cancer_model = joblib.load("models/lung_cancer_model.pkl")


st.title("AI-Powered Medical Diagnosis System")

disease = st.sidebar.selectbox(
    "Select Disease",
    ["Parkinson's Disease", "Diabetes", "Heart Disease", "Lung Cancer"]
)

def get_user_input(disease):
    st.subheader(f"Enter Details for {disease}")
    inputs = {}
    
    if disease == "Parkinson's Disease":
        inputs["MDVP:Fo(Hz)"] = st.number_input("MDVP:Fo(Hz)", key="MDVP_Fo_Hz")
        inputs["MDVP:Fhi(Hz)"] = st.number_input("MDVP:Fhi(Hz)", key="MDVP_Fhi_Hz")
        inputs["MDVP:Flo(Hz)"] = st.number_input("MDVP:Flo(Hz)", key="MDVP_Flo_Hz")
        inputs["MDVP:Jitter(%)"] = st.number_input("MDVP:Jitter(%)", key="MDVP_Jitter_percent")
        inputs["MDVP:Jitter(Abs)"] = st.number_input("MDVP:Jitter(Abs)", key="MDVP_Jitter_Abs")
        inputs["MDVP:Shimmer"] = st.number_input("MDVP:Shimmer", key="MDVP_Shimmer")
        inputs["HNR"] = st.number_input("HNR", key="HNR")
        inputs["RPDE"] = st.number_input("RPDE", key="RPDE")
        inputs["DFA"] = st.number_input("DFA", key="DFA")
        inputs["PPE"] = st.number_input("PPE", key="PPE")
    
    elif disease == "Diabetes":
        inputs["Pregnancies"] = st.number_input("Pregnancies", key="Pregnancies")
        inputs["Glucose"] = st.number_input("Glucose", key="Glucose")
        inputs["BloodPressure"] = st.number_input("BloodPressure", key="BloodPressure")
        inputs["SkinThickness"] = st.number_input("SkinThickness", key="SkinThickness")
        inputs["Insulin"] = st.number_input("Insulin", key="Insulin")
        inputs["BMI"] = st.number_input("BMI", key="BMI")
        inputs["DiabetesPedigreeFunction"] = st.number_input("Diabetes Pedigree Function", key="DiabetesPedigreeFunction")
        inputs["Age"] = st.number_input("Age", key="Age")
    
    elif disease == "Heart Disease":
        inputs["age"] = st.number_input("Age", key="age")
        inputs["sex"] = st.number_input("Sex (1 = male, 0 = female)", key="sex")
        inputs["cp"] = st.number_input("Chest Pain Type (0-3)", key="cp")
        inputs["trestbps"] = st.number_input("Resting Blood Pressure", key="trestbps")
        inputs["chol"] = st.number_input("Cholesterol", key="chol")
        inputs["fbs"] = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)", key="fbs")
        inputs["restecg"] = st.number_input("Resting ECG Results (0-2)", key="restecg")
        inputs["thalach"] = st.number_input("Maximum Heart Rate Achieved", key="thalach")
        inputs["exang"] = st.number_input("Exercise-Induced Angina (1 = yes, 0 = no)", key="exang")
        inputs["oldpeak"] = st.number_input("ST Depression Induced by Exercise", key="oldpeak")
        inputs["slope"] = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", key="slope")
        inputs["ca"] = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", key="ca")
        inputs["thal"] = st.number_input("Thalassemia (0-3)", key="thal")
    
    elif disease == "Lung Cancer":
        inputs["Age"] = st.number_input("Age", key="Age_lung")
        inputs["Smokes"] = st.number_input("Smokes (Packets per Year)", key="Smokes")
        inputs["AreaQ"] = st.number_input("AreaQ (Pollution Level)", key="AreaQ")
        inputs["Alkhol"] = st.number_input("Alcohol Consumption (Units per Week)", key="Alkhol")
    
    return pd.DataFrame([inputs])

user_input = get_user_input(disease)

if st.button("Predict"):
    if disease == "Parkinson's Disease":
        prediction = parkinson_model.predict(user_input)
    elif disease == "Diabetes":
        prediction = diabetes_model.predict(user_input)
    elif disease == "Heart Disease":
        prediction = heart_disease_model.predict(user_input)
    elif disease == "Lung Cancer":
        prediction = lung_cancer_model.predict(user_input)

    st.subheader("Prediction")
    if prediction[0] == 1:
        st.error("You are having the disease..!")
    else:
        st.success("You are healthy..!")
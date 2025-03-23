# 🩺 AI-Powered Medical Diagnosis System

This project is a **Streamlit-based web application** that predicts the likelihood of certain diseases using machine learning models. It currently supports **Parkinson's Disease, Diabetes, Heart Disease, and Lung Cancer** prediction based on various health parameters.

---

## 🚀 Features

- **Disease Selection**: Choose between different diseases (Parkinson's Disease, Diabetes, Heart Disease, Lung Cancer) for prediction.
- **User Input Fields**: Enter relevant health parameters such as glucose levels, BMI, smoking history, and more.
- **Prediction Output**: Displays whether the user is healthy or at risk of the disease.
- **Easy-to-Use Interface**: Built with **Streamlit** for a clean and interactive web-based experience.

---

## ⚙️ Technologies Used

- **Python**: For data processing and model training.
- **Streamlit**: For building the web interface.
- **Machine Learning**: For disease prediction.
- **Pandas & NumPy**: For data manipulation.
- **Scikit-Learn**: For building and training the models.
- **Joblib**: For saving and loading trained models.

---
## 🛠️ Installation & Usage

1. **Clone the repository:**  
```bash
git clone <repository_link>
cd <project_folder>
```
2. **Install the dependencies:**  
```bash
pip install -r requirements.txt
```
3. **Clean the Dataset:**  
```bash
python clean_datasets.py
```
4. **Train the Models:**  
```bash
python train_models.py
```
5. **Run the App:**  
```bash
streamlit run app.py
```

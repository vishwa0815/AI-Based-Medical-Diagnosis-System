import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_and_save_model(dataset_path, model_path, disease):
    data = pd.read_csv(dataset_path)
    
    if disease == "Parkinson's Disease":
        features = [
            "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", 
            "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:Shimmer", 
            "HNR", "RPDE", "DFA", "PPE"
        ]
        X = data[features]
    else:
        X = data.iloc[:, :-1]
    
    y = data.iloc[:, -1]

    if y.dtype == 'float':
        y = (y >= 0.5).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy for {model_path} ---- {accuracy * 100:.2f}%\n")

    joblib.dump(model, model_path)

train_and_save_model("datasets/parkinson_disease_cleaned.csv", "models/parkinson_model.pkl", "Parkinson's Disease")
train_and_save_model("datasets/diabetes_cleaned.csv", "models/diabetes_model.pkl", "Diabetes")
train_and_save_model("datasets/heart_disease_cleaned.csv", "models/heart_disease_model.pkl", "Heart Disease")
train_and_save_model("datasets/lung_cancer_cleaned.csv", "models/lung_cancer_model.pkl", "Lung Cancer")
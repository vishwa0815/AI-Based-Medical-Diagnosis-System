import pandas as pd

# Clean Parkinson's Disease Dataset
parkinson_data = pd.read_csv("datasets/parkinson_disease.csv")
parkinson_data = parkinson_data.drop(columns=["name"]) 
parkinson_data.to_csv("datasets/parkinson_disease_cleaned.csv", index=False)

# Clean Diabetes Dataset
diabetes_data = pd.read_csv("datasets/diabetes.csv")
diabetes_data.to_csv("datasets/diabetes_cleaned.csv", index=False) 

# Clean Heart Disease Dataset
heart_data = pd.read_csv("datasets/heart_disease.csv")
heart_data.to_csv("datasets/heart_disease_cleaned.csv", index=False) 

# Clean Lung Cancer Dataset
lung_cancer_data = pd.read_csv("datasets/lung_cancer.csv")
lung_cancer_data = lung_cancer_data.drop(columns=["Name", "Surname"])
lung_cancer_data.to_csv("datasets/lung_cancer_cleaned.csv", index=False)

print("All datasets cleaned and saved.")
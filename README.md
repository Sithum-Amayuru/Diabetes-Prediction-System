# Diabetes-Prediction-System
A Machine Learning web application that predicts diabetes risk using a Support Vector Machine (SVM) classifier. Features a user-friendly interface built with Streamlit and standardized medical data processing
🚀 Live Demo
[Paste your Streamlit Cloud Link Here - Optional]

Project Overview
The core of this project is a Support Vector Machine (SVM) classifier. I chose SVM because it is highly effective at finding the optimal "hyperplane" that separates data points into categories—in this case, Diabetic and Non-Diabetic.

Key Features:
Algorithm: SVM with a Linear Kernel.

Accuracy: Achieved a test accuracy of approximately 77-82%.

Real-time Prediction: A Streamlit-based UI where users can input medical data and get instant results.

Data Standardization: Implemented StandardScaler to ensure medical features like Glucose and Insulin are weighted equally by the model.

🛠️ Tech Stack
Language: Python 3.x

Machine Learning: Scikit-Learn

Data Handling: Pandas, NumPy

Visualization: Seaborn, Matplotlib

Web Framework: Streamlit

Model Serialization: Pickle

📊 Dataset Information
The model was trained on the PIMA Diabetes Dataset (Kaggle). It uses the following medical features:

Pregnancies

Glucose Level

Blood Pressure

Skin Thickness

Insulin Level

BMI

Diabetes Pedigree Function

Age

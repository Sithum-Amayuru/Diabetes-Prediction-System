# Diabetes-Prediction-System
A Machine Learning web application that predicts diabetes risk using a Support Vector Machine (SVM) classifier. Features a user-friendly interface built with Streamlit and standardized medical data processing
# Live Demo
Check out the live application here: [Diabetes Prediction Web App] https://diabetes-prediction-system-dsqnm6rzqfht5eevxulwwi.streamlit.app/
# Project Overview
The core of this project is a Support Vector Machine (SVM) classifier. I chose SVM because it is highly effective at finding the optimal "hyperplane" that separates data points into categories—in this case, Diabetic and Non-Diabetic.

# Key Features:
Algorithm: SVM with a Linear Kernel.

Accuracy: Achieved a test accuracy of approximately 77-82%.

Real-time Prediction: A Streamlit-based UI where users can input medical data and get instant results.

Data Standardization: Implemented StandardScaler to ensure medical features like Glucose and Insulin are weighted equally by the model.

# Tech Stack
1) Language: Python 3.x

2) Machine Learning: Scikit-Learn

3) Data Handling: Pandas, NumPy

4) Visualization: Seaborn, Matplotlib

5) Web Framework: Streamlit

6) Model Serialization: Pickle

# Dataset Information
The model was trained on the PIMA Diabetes Dataset (Kaggle). It uses the following medical features:

1) Pregnancies

2) Glucose Level

3) Blood Pressure

4) Skin Thickness

5) Insulin Level

6) BMI

7) Diabetes Pedigree Function

8) Age
   
## Technical Details

### Model Architecture
- **Algorithm:** Support Vector Machine (SVM)
- **Kernel:** Linear
- **Preprocessing:** Standard Scaling (`StandardScaler`)

### Performance
- **Training Accuracy:** ~78-80%
- **Test Accuracy:** ~77-79%

The model uses the **PIMA Indians Diabetes Dataset**. The primary focus was on **Glucose levels** and **BMI**, which showed the highest correlation with diabetes risk during Exploratory Data Analysis (EDA).

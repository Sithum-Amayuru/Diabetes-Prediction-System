import numpy as np
import pickle
import streamlit as st

# Load model and scaler
model_path = r'C:\Users\Lapmart.lk\Downloads\Diabetes_project\Diabetes_trained_model.sav'
scaler_path = r'C:\Users\Lapmart.lk\Downloads\Diabetes_project\scaler.sav'

loaded_model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))


def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    reshaped_input_data = input_data_as_numpy_array.reshape(1, -1)

    # Apply scaling
    std_data = scaler.transform(reshaped_input_data)

    prediction = loaded_model.predict(std_data)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


def main():
    st.title('Diabetes Prediction Web App')

    Pregnancies = st.number_input('Number of pregnancies', min_value=0)
    Glucose = st.number_input('Glucose level')
    BloodPressure = st.number_input('Blood pressure')
    SkinThickness = st.number_input('Skin thickness')
    Insulin = st.number_input('Insulin level')
    BMI = st.number_input('BMI')
    DiabetesPedigreeFunction = st.number_input('Diabetes pedigree function')
    Age = st.number_input('Age', min_value=0)

    if st.button('Diabetes Prediction Test Result'):
        input_data = [
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]

        result = diabetes_prediction(input_data)
        st.success(result)


if __name__ == '__main__':
    main()
import os
import pickle
import numpy as np
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model, scaler, and label encoder dictionary
weights_folder = "weights"
model_file_name = "credit_risk_model.pkl"
scaler_file_name = "standard_scaler.pkl"
encoder_file_name = "dict_all.obj"

# Load model
with open(os.path.join(weights_folder, model_file_name), 'rb') as model_file:
    model = pickle.load(model_file)

# Load scaler
with open(os.path.join(weights_folder, scaler_file_name), 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Load label encoding dictionary
with open(os.path.join(weights_folder, encoder_file_name), 'rb') as encoder_file:
    dict_all = pickle.load(encoder_file)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract the data from the form
    person_age = float(request.form['person_age'])
    person_income = float(request.form['person_income'])
    person_home_ownership = request.form['person_home_ownership']
    person_emp_length = float(request.form['person_emp_length'])
    loan_intent = request.form['loan_intent']
    loan_grade = request.form['loan_grade']
    loan_amnt = float(request.form['loan_amnt'])
    loan_int_rate = float(request.form['loan_int_rate'])
    loan_percent_income = float(request.form['loan_percent_income'])
    cb_person_default_on_file = request.form['cb_person_default_on_file']
    cb_person_cred_hist_length = float(request.form['cb_person_cred_hist_length'])

    # Encode categorical features using the dict_all encoding
    person_home_ownership = dict_all['person_home_ownership'][person_home_ownership]
    loan_intent = dict_all['loan_intent'][loan_intent]
    loan_grade = dict_all['loan_grade'][loan_grade]
    cb_person_default_on_file = dict_all['cb_person_default_on_file'][cb_person_default_on_file]

    # Prepare the data for prediction (make sure it is a 2D array)
    data = np.array([[person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]])

    # Scale the data using the pre-fitted scaler
    data_scaled = scaler.transform(data)

    # Make prediction using the pre-trained model
    prediction = model.predict(data_scaled)

    # Display result
    result = "Risk of Default" if prediction == 1 else "No Risk of Default"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

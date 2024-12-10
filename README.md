# Credit-Risk-Prediction

This project aims to predict the credit risk using machine learning models. It leverages a Flask web application for users to input their financial data and receive a prediction regarding the risk of default.

## Web Application

You can access the live web application here:  
[Credit Risk Prediction Web Application](https://credit-risk-prediction-r57n.onrender.com)

## Features

- **Predict credit risk**: The app allows users to input personal financial details such as age, income, loan amount, and other relevant features.
- **Custom Trained Model**: The app uses a custom-trained XGBoost machine learning model (stored as a pickle file) to predict whether a person is at risk of defaulting on a loan. The model was built using a dataset and fine-tuned for this specific credit risk prediction task.
- **User-friendly Interface**: The app provides an easy-to-use form to submit user data and shows the prediction result on the same page.
- **Prediction Output**: After submitting the form, the model predicts whether the user has a "Risk of Default" or "No Risk of Default".

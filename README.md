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

## Setup and Running Procedure

Follow the steps below to set up and run the Credit Risk Prediction web application locally:

### Prerequisites

Ensure that you have the following installed:

- Python 3.7 or higher
- pip (Python's package installer)

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/credit-risk-prediction.git
```

### Navigate to the Project Directory

Go to the project folder:

```bash
cd credit-risk-prediction
```

### Install the Required Dependencies

Install the necessary Python packages using pip. Run the following command inside the project directory:

```bash
pip install -r requirements.txt
```

This will install all the dependencies specified in the requirements.txt file, including Flask, XGBoost, and other required libraries.

### Run the Flask Application

To start the Flask web server, run the following command:

```bash
python app.py
```

### Access the Web Application

Open a web browser and go to the following URL to use the web application:

```bash
http://127.0.0.1:5000
```

### Predict Credit Risk

- On the home page, you will find a form where you can input financial details.
- After submitting the form, the app will use the custom-trained model to predict whether you have a "Risk of Default" or "No Risk of Default."
- The result will be shown on the same page, and you can view your prediction.

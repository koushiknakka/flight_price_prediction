# ✈️ Flight Price Prediction Model

This is a machine learning project that predicts flight ticket prices based on multiple travel-related parameters. The model is deployed using **Streamlit** to provide an interactive and user-friendly web interface.

---

## 🔍 Overview

- Built a regression model to predict flight prices.
- Utilized **Random Forest Regressor** as the primary model.
- Achieved an accuracy of **~98%** using RFR.
- Compared with other models:
  - **Lasso**, **Ridge**, and **ElasticNet** regressors achieved around **90%** accuracy.
- Performed **feature engineering** and **one-hot encoding** using `pandas.get_dummies()` due to the presence of multiple categorical features.

---

## 🚀 Features

- Predicts flight price using inputs like:
  - Airline
  - Source and Destination
  - Date of Journey
  - Departure and Arrival Time
  - Total Stops
  - Duration
- Clean and intuitive **Streamlit UI** for better user experience.
- Trained on cleaned and preprocessed dataset.

---

## 🧠 Model Performance

| Model                   | Accuracy (R² Score) |
|------------------------|---------------------|
| **Random Forest**       | **~98%**            |
| Lasso Regression        | ~90%                |
| Ridge Regression        | ~90%                |
| ElasticNet Regression   | ~90%                |

---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flight-price-prediction.git
   cd flight-price-prediction

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run StreamLit app**
   ```bash
   streamlit run app1.py

## 📌 Libraries Used

📌 Libraries Used

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- streamlit


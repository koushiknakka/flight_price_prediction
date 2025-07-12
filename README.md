✈️ Flight Price Prediction Model
This project is a machine learning-based web application that predicts the price of flights based on various travel details provided by the user. It uses the Random Forest Regressor algorithm, along with other regression techniques, and offers a clean user experience through a Streamlit-based interface.

📌 Features
Predicts flight prices based on input parameters like source, destination, airline, departure time, etc.

Uses Random Forest Regressor for high-accuracy prediction (~98%).

Compared performance with Lasso, Ridge, and ElasticNet (each ~90% accuracy).

Clean UI with Streamlit for seamless user interaction.

Encodes categorical variables using Pandas get_dummies() for handling multiple classifiers.

🧠 Model Overview
Regression Model	Accuracy Score
Random Forest Regressor	~98%
Lasso Regression	~90%
Ridge Regression	~90%
ElasticNet Regression	~90%

The Random Forest model outperformed others in terms of R² score and generalization.

Trained on a cleaned dataset with extracted features such as journey date, duration, total stops, and more.

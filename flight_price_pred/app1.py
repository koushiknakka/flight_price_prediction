import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('flight_price_model.pkl')

st.title("✈️ Flight Price Prediction App")

# Input widgets
stops = st.selectbox("Number of Stops", [0, 1, 2, 3, 4])
flight_class = st.selectbox("Class (0: Economy, 1: Business)", [0, 1])
duration = st.slider("Duration (hours)", min_value=0.83,max_value=49.83, step=0.01)
days_left = st.slider("Days left for flight", min_value=1,max_value=49, step=1)

airline = st.selectbox("Airline", ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo','Air_India'])
source = st.selectbox("Source City", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
destination = st.selectbox("Destination City",  ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])

dep_time = st.selectbox("Departure Time", ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
       'Late_Night'])
arr_time = st.selectbox("Arrival Time", ['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening','Late_Night'])

# Build feature array
airline_map = ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo','Air_India']
source_map =  ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
destination_map =  ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
dep_map = ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
       'Late_Night']
arr_map = ['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening','Late_Night']

features = []

# Add basic features
features.append(stops)
features.append(flight_class)
features.append(duration)
features.append(days_left)

# Airline dummies
for a in airline_map:
    features.append(1 if airline == a else 0)

# Source dummies
for s in source_map:
    features.append(1 if source == s else 0)

# Destination dummies
for d in destination_map:
    features.append(1 if destination == d else 0)

# Departure time dummies
for t in dep_map:
    features.append(1 if dep_time == t else 0)

for t in arr_map:
    features.append(1 if arr_time == t else 0)

# Convert to numpy array
features = np.array([features])

# Predict
if st.button("Predict Price"):
    price = model.predict(features)[0]
    st.success(f"💸 Estimated Flight Price: ₹ {int(price)}")